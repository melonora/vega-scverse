from pathlib import Path
import inspect
from . import specification, scales, data

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "specification.yaml"

# Create a list of all classes from specification.py
__all__ = []

modules = [
    'vega_scverse.spec_models.specification',
    'vega_scverse.spec_models.scales',
    'vega_scverse.spec_models.data',
]
objects = [
    *inspect.getmembers(specification),
    *inspect.getmembers(scales),
    *inspect.getmembers(data),
]

for name, obj in objects:
    if inspect.isclass(obj) and obj.__module__ in modules:
        __all__.append(name)
