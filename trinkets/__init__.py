import sys
import faulthandler
if not faulthandler.is_enabled():
    faulthandler.enable()

def configure_default_logging():
    """
    Simple logging configuration.
    Useful for interactive terminal sessions.
    """
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.handlers = []
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

from .view_as_blocks import view_as_blocks
from .csv import *
from .table import *
from .box import *
from .grid import *
from .sparse_block_mask import *
from .graph import *
from .segmentation import *
from .downsample_with_numba import *
from .util import *
from .skeleton import *
