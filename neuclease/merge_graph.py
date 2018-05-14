import logging
import threading
from collections import defaultdict

import numpy as np
import pandas as pd

from .util import Timer
from .rwlock import ReadWriteLock
from .dvid import fetch_supervoxels_for_body, fetch_label_for_coordinate, fetch_mappings, fetch_mutation_id
from .merge_table import load_edge_csv, load_mapping, load_merge_table, normalize_merge_table, apply_mapping_to_mergetable

_logger = logging.getLogger(__name__)

class LabelmapMergeGraph:
    """
    Represents a volume-wide merge graph.
    The set of all possible edges are immutable, and initialized from a immutable merge table,
    but the edges for each body are extracted from the total set according to their
    dynamically-queried supervoxel members.
    """
        
    def __init__(self, table_path, mapping=None, primary_uuid=None):
        self.rwlock = ReadWriteLock()
        self.primary_uuid = primary_uuid

        if isinstance(mapping, str):
            mapping = load_mapping(mapping)

        self.merge_table_df = load_merge_table(table_path, mapping, normalize=True)
        self._mapping_versions = {}
        
        # Supervoxels retrieved from DVID are cached in this member.
        self._sv_cache = {}
        
        # This lock protects the above cache
        self._sv_cache_main_lock = threading.Lock()
        
        # This dict holds a lock for each body, to avoid requesting supervoxels for the same body in parallel,
        # (but requesting supervoxels for different bodies in parallel is OK).
        self._sv_cache_key_locks = defaultdict(lambda: threading.Lock())
    

    def append_edges_for_split_supervoxels(self, split_mapping, server, uuid, instance):
        """
        Append edges to the merge table for the given split supervoxels (do not remove edges for their parents).
        
        Args:
            split_mapping:
                A mapping (2-column numpy array) of [[child, parent], [child,parent],...] or a path from which it can be loaded.
            
            server, uuid, instance:
                Identifies a DVID labelmap instance from which new supervoxel IDs
                can be queried via points in the DVID labelmap volume.
        Returns:
            If any edges could not be preserved because the queried point in DVID does not seem to be a split child,
            a DataFrame of such edges is returned.
        """
        if isinstance(split_mapping, str):
            split_mapping = load_edge_csv(split_mapping)

        assert np.unique(split_mapping[:,0]).shape[0] == split_mapping.shape[0], \
            "Split mapping should be given as [[child, parent],...], not [parent, child] (and every child should have only one parent)."

        # First extract relevant rows for faster queries below
        children = set(split_mapping[:,0])
        _parents = set(split_mapping[:,1])
        update_table_df = self.merge_table_df.query('id_a in @_parents or id_b in @_parents').copy()
        assert update_table_df.columns[:2].tolist() == ['id_a', 'id_b']

        with Timer(f"Appending {len(update_table_df)} edges with split supervoxel IDs", _logger):
            bad_edges = []
            for i in range(len(update_table_df)):
                row = update_table_df.iloc[i:i+1]
                coord_a = row[['za', 'ya', 'xa']].values[0]
                coord_b = row[['zb', 'yb', 'xb']].values[0]
                
                if (coord_a == (0,0,0)).all() or (coord_b == (0,0,0)).all():
                    assert False, "FIXME"
                
                sv_a = fetch_label_for_coordinate(server, uuid, instance, coord_a, supervoxels=True)
                sv_b = fetch_label_for_coordinate(server, uuid, instance, coord_b, supervoxels=True)

                # If either coordinate returns a non-sensical point, then
                # the provided split mapping does not match the currently stored labels.
                if sv_a not in children and sv_b not in children:
                    if sv_a not in children and sv_a != update_table_df.iloc[i, 0]:
                        bad_edges.append(('a', sv_a) + tuple(update_table_df.iloc[i]))
                    if sv_b not in children and sv_b != update_table_df.iloc[i, 1]:
                        bad_edges.append(('b', sv_b) + tuple(update_table_df.iloc[i]))
                else:
                    update_table_df.iloc[i, 0] = sv_a # id_a
                    update_table_df.iloc[i, 1] = sv_b # id_b

        if bad_edges:
            # FIXME: Rows with 'bad edges' were not updated with new SV ids,
            #        meaning that they remain duplicates of the original rows.
            #        we should remove them from update_table_df before appending to self.merge_table_df 
            bad_edges = pd.DataFrame(bad_edges, columns=['end', 'found_sv'] + list(update_table_df.columns))
        else:
            bad_edges = update_table_df.iloc[:0] # No bad edges: Empty DataFrame

        # Normalize the updates
        normalized_update = normalize_merge_table(update_table_df.drop('body', axis=1).to_records(index=False))
        normalized_update_df = pd.DataFrame(normalized_update, index=update_table_df.index)
        normalized_update_df['body'] = update_table_df['body']

        # Append the updates
        self.merge_table_df = pd.concat((self.merge_table_df, normalized_update_df), ignore_index=True, copy=False)

        return bad_edges

    def fetch_and_apply_mapping(self, server, uuid, labelmap_instance):
        mapping = fetch_mappings(server, uuid, labelmap_instance, True)
        apply_mapping_to_mergetable(self.merge_table_df, mapping)


    def fetch_supervoxels_for_body(self, dvid_server, uuid, labelmap_instance, body_id, logger=_logger):
        """
        Fetch the supervoxels for the given body from DVID.
        The results are cached internally, according to the body's current mutation id.
        
        Returns:
            (mutation id, supervoxels)
        """
        key = (dvid_server, uuid, labelmap_instance, body_id)
        mut_id = fetch_mutation_id(dvid_server, uuid, labelmap_instance, body_id)

        with self._sv_cache_main_lock:
            key_lock = self._sv_cache_key_locks[key]

        # Use a lock to avoid requesting the supervoxels from DVID in-parallel,
        # in case the user sends several requests at once for the same body,
        # which can happen if they click faster than dvid can respond.
        with key_lock:
            if key in self._sv_cache:
                cached_mut_id, supervoxels = self._sv_cache[key]
                if cached_mut_id == mut_id:
                    return mut_id, supervoxels # Cache is up-to-date
            
            with Timer() as timer:
                supervoxels = fetch_supervoxels_for_body(dvid_server, uuid, labelmap_instance, body_id)
                supervoxels = np.asarray(supervoxels, np.uint64)
                supervoxels.sort()

            # Save in cache
            with self._sv_cache_main_lock:
                self._sv_cache[key] = (mut_id, supervoxels)

        logger.info(f"Retrieving supervoxel list from DVID took {timer.timedelta}")
        return mut_id, supervoxels


    def extract_rows(self, dvid_server, uuid, labelmap_instance, body_id, logger=None):
        """
        Determine which supervoxels belong to the given body,
        and extract all edges involving those supervoxels (and only those supervoxels).
        """
        body_id = np.uint64(body_id)
        if logger is None:
            logger = _logger
        
        mut_id, dvid_supervoxels = self.fetch_supervoxels_for_body(dvid_server, uuid, labelmap_instance, body_id, logger)

        with self.rwlock.context(write=False):
            try:
                mapping_is_in_sync = (self._mapping_versions[body_id] == (dvid_server, uuid, labelmap_instance, mut_id))
            except KeyError:
                mapping_is_in_sync = False

            # It's very fast to select rows based on the body_id,
            # so we prefer that if the mapping is already in sync with DVID.
            body_positions_orig = (self.merge_table_df['body'] == body_id).values.nonzero()[0]
            subset_df = self.merge_table_df.iloc[body_positions_orig]
            svs_from_table = np.unique(subset_df[['id_a', 'id_b']].values)

            if mapping_is_in_sync:
                return subset_df, dvid_supervoxels

            # Maybe the mapping isn't in sync, but the supervoxels match anyway...
            if svs_from_table.shape == dvid_supervoxels.shape and (svs_from_table == dvid_supervoxels).all():
                self._mapping_versions[body_id] = (dvid_server, uuid, labelmap_instance, mut_id)
                return subset_df, dvid_supervoxels

        # If we get this far, our mapping is out-of-sync with DVID's agglomeration.
        # Query for the rows the slow way (via set membership).
        # 
        # Note:
        #    I tried speeding this up using proper index-based pandas selection:
        #        merge_table_df.loc[(supervoxels, supervoxels), 'body'] = body_id
        #    ...but that is MUCH worse for large selections, and only marginally
        #    faster for small selections.
        #    Using eval() seems to be the best option here.
        #    The worst body we've got takes ~30 seconds to extract.

        # Should we overwrite the body column for these rows?
        permit_write = (self.primary_uuid is None or uuid == self.primary_uuid)
        with self.rwlock.context(permit_write):
            # Must re-query the rows to change, since the table might have changed while the lock was released.
            body_positions_orig = (self.merge_table_df['body'] == body_id).values.nonzero()[0]
            logger.info(f"Cached supervoxels (N={len(svs_from_table)}) don't match expected (N={len(dvid_supervoxels)}).  Updating cache.")
            _sv_set = set(dvid_supervoxels)
            subset_positions = self.merge_table_df.eval('id_a in @_sv_set and id_b in @_sv_set').values
            subset_df = self.merge_table_df.iloc[subset_positions].copy()
            subset_df['body'] = body_id

            if permit_write:
                # Before we overwrite, invalidate the mapping version for any body IDs we're about to overwrite
                for prev_body in pd.unique(subset_df['body'].values):
                    if prev_body in self._mapping_versions:
                        del self._mapping_versions[prev_body]

                self._mapping_versions[body_id] = (dvid_server, uuid, labelmap_instance, mut_id)
                self.merge_table_df['body'].values[body_positions_orig] = 0
                self.merge_table_df['body'].values[subset_positions] = body_id
    
            return subset_df, dvid_supervoxels

