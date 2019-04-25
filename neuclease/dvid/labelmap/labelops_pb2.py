# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: neuclease/dvid/labelmap/labelops.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='neuclease/dvid/labelmap/labelops.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&neuclease/dvid/labelmap/labelops.proto\x12\x05proto\"8\n\x07MergeOp\x12\r\n\x05mutid\x18\x01 \x01(\x04\x12\x0e\n\x06target\x18\x02 \x01(\x04\x12\x0e\n\x06merged\x18\x03 \x03(\x04\"<\n\tMappingOp\x12\r\n\x05mutid\x18\x01 \x01(\x04\x12\x0e\n\x06mapped\x18\x02 \x01(\x04\x12\x10\n\x08original\x18\x03 \x03(\x04\"0\n\nMappingOps\x12\"\n\x08mappings\x18\x01 \x03(\x0b\x32\x10.proto.MappingOp\"X\n\x07SplitOp\x12\r\n\x05mutid\x18\x01 \x01(\x04\x12\x0e\n\x06target\x18\x02 \x01(\x04\x12\x10\n\x08newlabel\x18\x03 \x01(\x04\x12\x0e\n\x06\x63oarse\x18\x04 \x01(\x08\x12\x0c\n\x04rles\x18\x05 \x01(\x0c\"+\n\x0bOpCompleted\x12\r\n\x05mutid\x18\x01 \x01(\x04\x12\r\n\x05stage\x18\x02 \x01(\t\"9\n\x08\x41\x66\x66inity\x12\x0e\n\x06label1\x18\x01 \x01(\x04\x12\x0e\n\x06label2\x18\x02 \x01(\x04\x12\r\n\x05value\x18\x03 \x01(\x02\"0\n\nAffinities\x12\x0e\n\x06labels\x18\x01 \x03(\x04\x12\x12\n\naffinities\x18\x02 \x03(\x02\"\x80\x01\n\rAffinityTable\x12.\n\x05table\x18\x01 \x03(\x0b\x32\x1f.proto.AffinityTable.TableEntry\x1a?\n\nTableEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.proto.Affinities:\x02\x38\x01\"d\n\x07SVCount\x12*\n\x06\x63ounts\x18\x01 \x03(\x0b\x32\x1a.proto.SVCount.CountsEntry\x1a-\n\x0b\x43ountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xcb\x01\n\nLabelIndex\x12-\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x1d.proto.LabelIndex.BlocksEntry\x12\r\n\x05label\x18\x02 \x01(\x04\x12\x12\n\nlast_mutid\x18\x03 \x01(\x04\x12\x15\n\rlast_mod_time\x18\x04 \x01(\t\x12\x15\n\rlast_mod_user\x18\x05 \x01(\t\x1a=\n\x0b\x42locksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.proto.SVCount:\x02\x38\x01\"2\n\x0cLabelIndices\x12\"\n\x07indices\x18\x01 \x03(\x0b\x32\x11.proto.LabelIndexb\x06proto3')
)




_MERGEOP = _descriptor.Descriptor(
  name='MergeOp',
  full_name='proto.MergeOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mutid', full_name='proto.MergeOp.mutid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='proto.MergeOp.target', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merged', full_name='proto.MergeOp.merged', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=105,
)


_MAPPINGOP = _descriptor.Descriptor(
  name='MappingOp',
  full_name='proto.MappingOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mutid', full_name='proto.MappingOp.mutid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapped', full_name='proto.MappingOp.mapped', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original', full_name='proto.MappingOp.original', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=167,
)


_MAPPINGOPS = _descriptor.Descriptor(
  name='MappingOps',
  full_name='proto.MappingOps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mappings', full_name='proto.MappingOps.mappings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=217,
)


_SPLITOP = _descriptor.Descriptor(
  name='SplitOp',
  full_name='proto.SplitOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mutid', full_name='proto.SplitOp.mutid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='proto.SplitOp.target', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newlabel', full_name='proto.SplitOp.newlabel', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coarse', full_name='proto.SplitOp.coarse', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rles', full_name='proto.SplitOp.rles', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=307,
)


_OPCOMPLETED = _descriptor.Descriptor(
  name='OpCompleted',
  full_name='proto.OpCompleted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mutid', full_name='proto.OpCompleted.mutid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='proto.OpCompleted.stage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=352,
)


_AFFINITY = _descriptor.Descriptor(
  name='Affinity',
  full_name='proto.Affinity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label1', full_name='proto.Affinity.label1', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label2', full_name='proto.Affinity.label2', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.Affinity.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=411,
)


_AFFINITIES = _descriptor.Descriptor(
  name='Affinities',
  full_name='proto.Affinities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='proto.Affinities.labels', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='affinities', full_name='proto.Affinities.affinities', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=461,
)


_AFFINITYTABLE_TABLEENTRY = _descriptor.Descriptor(
  name='TableEntry',
  full_name='proto.AffinityTable.TableEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.AffinityTable.TableEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.AffinityTable.TableEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=592,
)

_AFFINITYTABLE = _descriptor.Descriptor(
  name='AffinityTable',
  full_name='proto.AffinityTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='proto.AffinityTable.table', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_AFFINITYTABLE_TABLEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=592,
)


_SVCOUNT_COUNTSENTRY = _descriptor.Descriptor(
  name='CountsEntry',
  full_name='proto.SVCount.CountsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.SVCount.CountsEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.SVCount.CountsEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=649,
  serialized_end=694,
)

_SVCOUNT = _descriptor.Descriptor(
  name='SVCount',
  full_name='proto.SVCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counts', full_name='proto.SVCount.counts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SVCOUNT_COUNTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=694,
)


_LABELINDEX_BLOCKSENTRY = _descriptor.Descriptor(
  name='BlocksEntry',
  full_name='proto.LabelIndex.BlocksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.LabelIndex.BlocksEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.LabelIndex.BlocksEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=900,
)

_LABELINDEX = _descriptor.Descriptor(
  name='LabelIndex',
  full_name='proto.LabelIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='proto.LabelIndex.blocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='proto.LabelIndex.label', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mutid', full_name='proto.LabelIndex.last_mutid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mod_time', full_name='proto.LabelIndex.last_mod_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mod_user', full_name='proto.LabelIndex.last_mod_user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LABELINDEX_BLOCKSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=900,
)


_LABELINDICES = _descriptor.Descriptor(
  name='LabelIndices',
  full_name='proto.LabelIndices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='indices', full_name='proto.LabelIndices.indices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=902,
  serialized_end=952,
)

_MAPPINGOPS.fields_by_name['mappings'].message_type = _MAPPINGOP
_AFFINITYTABLE_TABLEENTRY.fields_by_name['value'].message_type = _AFFINITIES
_AFFINITYTABLE_TABLEENTRY.containing_type = _AFFINITYTABLE
_AFFINITYTABLE.fields_by_name['table'].message_type = _AFFINITYTABLE_TABLEENTRY
_SVCOUNT_COUNTSENTRY.containing_type = _SVCOUNT
_SVCOUNT.fields_by_name['counts'].message_type = _SVCOUNT_COUNTSENTRY
_LABELINDEX_BLOCKSENTRY.fields_by_name['value'].message_type = _SVCOUNT
_LABELINDEX_BLOCKSENTRY.containing_type = _LABELINDEX
_LABELINDEX.fields_by_name['blocks'].message_type = _LABELINDEX_BLOCKSENTRY
_LABELINDICES.fields_by_name['indices'].message_type = _LABELINDEX
DESCRIPTOR.message_types_by_name['MergeOp'] = _MERGEOP
DESCRIPTOR.message_types_by_name['MappingOp'] = _MAPPINGOP
DESCRIPTOR.message_types_by_name['MappingOps'] = _MAPPINGOPS
DESCRIPTOR.message_types_by_name['SplitOp'] = _SPLITOP
DESCRIPTOR.message_types_by_name['OpCompleted'] = _OPCOMPLETED
DESCRIPTOR.message_types_by_name['Affinity'] = _AFFINITY
DESCRIPTOR.message_types_by_name['Affinities'] = _AFFINITIES
DESCRIPTOR.message_types_by_name['AffinityTable'] = _AFFINITYTABLE
DESCRIPTOR.message_types_by_name['SVCount'] = _SVCOUNT
DESCRIPTOR.message_types_by_name['LabelIndex'] = _LABELINDEX
DESCRIPTOR.message_types_by_name['LabelIndices'] = _LABELINDICES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MergeOp = _reflection.GeneratedProtocolMessageType('MergeOp', (_message.Message,), dict(
  DESCRIPTOR = _MERGEOP,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.MergeOp)
  ))
_sym_db.RegisterMessage(MergeOp)

MappingOp = _reflection.GeneratedProtocolMessageType('MappingOp', (_message.Message,), dict(
  DESCRIPTOR = _MAPPINGOP,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.MappingOp)
  ))
_sym_db.RegisterMessage(MappingOp)

MappingOps = _reflection.GeneratedProtocolMessageType('MappingOps', (_message.Message,), dict(
  DESCRIPTOR = _MAPPINGOPS,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.MappingOps)
  ))
_sym_db.RegisterMessage(MappingOps)

SplitOp = _reflection.GeneratedProtocolMessageType('SplitOp', (_message.Message,), dict(
  DESCRIPTOR = _SPLITOP,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.SplitOp)
  ))
_sym_db.RegisterMessage(SplitOp)

OpCompleted = _reflection.GeneratedProtocolMessageType('OpCompleted', (_message.Message,), dict(
  DESCRIPTOR = _OPCOMPLETED,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.OpCompleted)
  ))
_sym_db.RegisterMessage(OpCompleted)

Affinity = _reflection.GeneratedProtocolMessageType('Affinity', (_message.Message,), dict(
  DESCRIPTOR = _AFFINITY,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.Affinity)
  ))
_sym_db.RegisterMessage(Affinity)

Affinities = _reflection.GeneratedProtocolMessageType('Affinities', (_message.Message,), dict(
  DESCRIPTOR = _AFFINITIES,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.Affinities)
  ))
_sym_db.RegisterMessage(Affinities)

AffinityTable = _reflection.GeneratedProtocolMessageType('AffinityTable', (_message.Message,), dict(

  TableEntry = _reflection.GeneratedProtocolMessageType('TableEntry', (_message.Message,), dict(
    DESCRIPTOR = _AFFINITYTABLE_TABLEENTRY,
    __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
    # @@protoc_insertion_point(class_scope:proto.AffinityTable.TableEntry)
    ))
  ,
  DESCRIPTOR = _AFFINITYTABLE,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.AffinityTable)
  ))
_sym_db.RegisterMessage(AffinityTable)
_sym_db.RegisterMessage(AffinityTable.TableEntry)

SVCount = _reflection.GeneratedProtocolMessageType('SVCount', (_message.Message,), dict(

  CountsEntry = _reflection.GeneratedProtocolMessageType('CountsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SVCOUNT_COUNTSENTRY,
    __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
    # @@protoc_insertion_point(class_scope:proto.SVCount.CountsEntry)
    ))
  ,
  DESCRIPTOR = _SVCOUNT,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.SVCount)
  ))
_sym_db.RegisterMessage(SVCount)
_sym_db.RegisterMessage(SVCount.CountsEntry)

LabelIndex = _reflection.GeneratedProtocolMessageType('LabelIndex', (_message.Message,), dict(

  BlocksEntry = _reflection.GeneratedProtocolMessageType('BlocksEntry', (_message.Message,), dict(
    DESCRIPTOR = _LABELINDEX_BLOCKSENTRY,
    __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
    # @@protoc_insertion_point(class_scope:proto.LabelIndex.BlocksEntry)
    ))
  ,
  DESCRIPTOR = _LABELINDEX,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.LabelIndex)
  ))
_sym_db.RegisterMessage(LabelIndex)
_sym_db.RegisterMessage(LabelIndex.BlocksEntry)

LabelIndices = _reflection.GeneratedProtocolMessageType('LabelIndices', (_message.Message,), dict(
  DESCRIPTOR = _LABELINDICES,
  __module__ = 'neuclease.dvid.labelmap.labelops_pb2'
  # @@protoc_insertion_point(class_scope:proto.LabelIndices)
  ))
_sym_db.RegisterMessage(LabelIndices)


_AFFINITYTABLE_TABLEENTRY._options = None
_SVCOUNT_COUNTSENTRY._options = None
_LABELINDEX_BLOCKSENTRY._options = None
# @@protoc_insertion_point(module_scope)
