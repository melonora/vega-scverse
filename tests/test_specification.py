from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import ViewConfiguration

DATA_DIR = Path(__file__).parent / "data" / "examples" / "full_examples"


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("image")]
)
def test_image_viewconfig(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ViewConfiguration)
    assert obj


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("label")]
)
def test_label_viewconfig(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ViewConfiguration)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("points")]
)
def test_points_viewconfig(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ViewConfiguration)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("shapes")]
)
def test_shapes_viewconfig(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=ViewConfiguration)
    assert obj