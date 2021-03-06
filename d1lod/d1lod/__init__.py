from . import people
from . import dataone
from . import util
from . import validator
from . import metadata
from .graph import Graph
from .interface import Interface

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
