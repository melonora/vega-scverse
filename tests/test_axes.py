from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import Axis

DATA_DIR = Path(__file__).parent / "data" / "examples" / "axes"

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("axes")]
)
def test_axes(json_path):
    """Ensure valid axes objects can be loaded."""
    obj = json_loader.load(json_path, target_class=Axis)
    assert obj
