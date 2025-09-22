from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import ImageEncode, LabelEncode, SymbolEncode

DATA_DIR = Path(__file__).parent / "data" / "examples" / "encode"


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("image")]
)
def test_image_encode(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ImageEncode)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("label")]
)
def test_label_encode(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=LabelEncode)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("symbol")]
)
def test_symbol_encode(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=SymbolEncode)
    assert obj