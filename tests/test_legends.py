from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import CategoricalLegend, ColorBarLegend

DATA_DIR = Path(__file__).parent / "data" / "examples" / "legends"


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("categorical")]
)
def test_categorical_legends(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=CategoricalLegend)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("colorbar")]
)
def test_colorbar_legends(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ColorBarLegend)
    assert obj