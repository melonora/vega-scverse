
from pathlib import Path
import pytest
from pydantic import ValidationError

from linkml_runtime.loaders import json_loader
from vega_scverse import Scales, AxisScale, CategoricalColorScale, LinearColorScale

DATA_DIR = Path(__file__).parent / "data" / "examples" / "scales"

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("scales")]
)
def test_scales(json_path):
    """Ensure complete scales object can be loaded."""
    obj = json_loader.load(json_path, target_class=Scales)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("linear")]
)
def test_continous_color_scales(json_path):
    obj = json_loader.load(json_path, target_class=LinearColorScale)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("axis")]
)
def test_axis_scales(json_path):
    obj = json_loader.load(json_path, target_class=AxisScale)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("categorical")]
)
def test_categorical_scales(json_path):
    obj = json_loader.load(json_path, target_class=CategoricalColorScale)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_axis")]
)
def test_invalid_axis_scales(json_path):
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=AxisScale)

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_categorical")]
)
def test_invalid_categorical_color_scales(json_path):
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=CategoricalColorScale)

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_linear")]
)
def test_invalid_linear_color_scales(json_path):
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=LinearColorScale)