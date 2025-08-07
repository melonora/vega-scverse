from pathlib import Path
import inspect
from . import specification
from . import scales

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "specification.yaml"

# Create a list of all classes from specification.py
__all__ = []
for name, obj in inspect.getmembers(specification):
    if inspect.isclass(obj) and obj.__module__ == 'vega_scverse.spec_models.specification':
        __all__.append(name)

for name, obj in inspect.getmembers(scales):
    if inspect.isclass(obj) and obj.__module__ == 'vega_scverse.spec_models.scales':
        __all__.append(name)
