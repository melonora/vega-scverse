from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import SpatialDataObject, TableObject
from pydantic import ValidationError

DATA_DIR = Path(__file__).parent / "data" / "examples" / "data"

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("sdata")]
)
def test_sdata(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=SpatialDataObject)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_sdata")]
)
def test_invalid_sdata(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=SpatialDataObject)

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("table")]
)
def test_sdata_table(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=TableObject)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_table")]
)
def test_sdata_table(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=TableObject)
