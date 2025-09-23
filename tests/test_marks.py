from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import RasterImageMark, RasterLabelMark, PointsMark, ShapesMark, TextMark, GroupMark

DATA_DIR = Path(__file__).parent / "data" / "examples" / "marks"


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("image")]
)
def test_image_marks(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=RasterImageMark)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("label")]
)
def test_label_marks(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=RasterLabelMark)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("points")]
)
def test_points_marks(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=PointsMark)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("shapes")]
)
def test_shapes_marks(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ShapesMark)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("text")]
)
def test_text_marks(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=TextMark)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("group")]
)
def test_group_marks(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=GroupMark)
    assert obj