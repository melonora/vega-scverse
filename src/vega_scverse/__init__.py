from .__about__ import __version__
from .spec_models.linkml_specification import *
from .spec_models.scales import *
from .spec_models.data import *
from .spec_models.marks import *
from .spec_models.specification import *

import inspect
from . import spec_models

# Create a list of all classes from specification.py
__all__ = ["__version__"]
for name, obj in inspect.getmembers(spec_models):
    if name == '__all__':
        __all__ += obj