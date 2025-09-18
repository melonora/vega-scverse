from pathlib import Path
import pytest

from linkml_runtime.loaders import json_loader
from vega_scverse import SpatialDataObject, TableObject, FilterTransform, FilterChannelTransform, AggregateTransform, \
    SpreadTransform, NormalizationFormulaTransform, SpatialDataElementObject
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
def test_inv_sdata_table(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=TableObject)

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("element")]
)
def test_sdata_element(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    obj = json_loader.load(json_path, target_class=SpatialDataElementObject)
    assert obj

@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("filter_transform")]
)
def test_filter_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    json_loader.load(json_path, target_class=FilterTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_filter_transform")]
)
def test_inv_filter_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=FilterTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("filter_channel")]
)
def test_filter_channel_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    json_loader.load(json_path, target_class=FilterChannelTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_filter_channel")]
)
def test_inv_filter_channel_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=FilterChannelTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("aggregate")]
)
def test_aggregate_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    json_loader.load(json_path, target_class=AggregateTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_aggregate")]
)
def test_inv_aggregate_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=AggregateTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("spread")]
)
def test_spread_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    json_loader.load(json_path, target_class=SpreadTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_spread")]
)
def test_inv_spread_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=SpreadTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("normalization")]
)
def test_normalization_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    json_loader.load(json_path, target_class=NormalizationFormulaTransform)


@pytest.mark.parametrize(
    "json_path",
    [p for p in DATA_DIR.glob("*.json") if p.stem.startswith("inv_normalization")]
)
def test_inv_normalization_transform(json_path):
    """Ensure complete sdata objects within data objects can be loaded."""
    with pytest.raises(ValidationError):
        json_loader.load(json_path, target_class=NormalizationFormulaTransform)
