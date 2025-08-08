
from pathlib import Path
import pytest
from pydantic import ValidationError

from linkml_runtime.loaders import json_loader
from vega_scverse import Axis

DATA_DIR = Path(__file__).parent / "data" / "examples" / "axes"

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("axes")]
)
def test_scales(json_path):
    """Ensure complete scales object can be loaded."""
    obj = json_loader.load(json_path, target_class=Axis)
    assert obj
