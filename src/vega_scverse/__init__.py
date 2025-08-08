from .__about__ import __version__
from .spec_models.specification import *
from .spec_models.scales import *


# Get all classes from specification.py
import inspect
from . import spec_models
from .spec_models import specification
from .spec_models import scales

# Create a list of all classes from specification.py
__all__ = ["__version__"]
for name, obj in inspect.getmembers(specification):
    if inspect.isclass(obj) and obj.__module__ == 'vega_scverse.spec_models.specification':
        __all__.append(name)

for name, obj in inspect.getmembers(scales):
    if inspect.isclass(obj) and obj.__module__ == 'vega_scverse.spec_models.scales':
        __all__.append(name)