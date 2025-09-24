from typing import Optional, Union

from .linkml_specification import BaseViewConfiguration, TextMark, SpatialDataObject
from pydantic import Field

from .scales import AxisScale, CategoricalColorScale
from .linkml_scales import LinearColorScale
from .marks import ShapesMark, RasterLabelMark, RasterImageMark, PointsMark, GroupMark
from .data import SpatialDataElementObject, TableObject


class ViewConfiguration(BaseViewConfiguration):
    schema: Optional[str] = Field(
        default="https://github.com/melonora/vega-scverse/blob/main/src/vega_scverse/schema/linkml_specification.yaml",
        description="""The schema version""",
        alias="$schema",
        json_schema_extra={
            "linkml_meta": {
                "alias": "$schema",
                "domain_of": ["BaseViewConfiguration"],
                "ifabsent": "string(https://github.com/melonora/vega-scverse/blob/main/src/vega_scverse/schema/linkml_specification.yaml)",
            }
        },
    )
    data: list[Union[SpatialDataElementObject, TableObject, SpatialDataObject]] = Field(
        default=...,
        description="""Scverse data set definitions and transforms define the data to load and how to process it.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "any_of": [
                    {"range": "SpatialDataObject"},
                    {"range": "BaseTableObject"},
                    {"range": "BaseSpatialDataElementObject"},
                ],
                "domain_of": ["ContinuousColorDomain", "MarkDataSource", "BaseViewConfiguration"],
            }
        },
    )
    scales: Optional[list[AxisScale | CategoricalColorScale | LinearColorScale]] = Field(
        default=None,
        description="""Scales map data values (numbers, dates, categories, etc.) to visual values (pixels, colors, sizes).
        Scales are a fundamental building block of data visualization, as they determine the nature of visual
        encodings.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "scales",
                "any_of": [
                    {"range": "BaseAxisScale"},
                    {"range": "BaseCategoricalColorScale"},
                    {"range": "LinearColorScale"},
                ],
                "domain_of": ["BaseScales", "BaseGroupMark"],
            }
        },
    )
    marks: list[
        Union[GroupMark, PointsMark, RasterImageMark, RasterLabelMark, ShapesMark, TextMark]
    ] = Field(
        default=...,
        description="""Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting
    symbols. Marks are the basic visual building block of a visualization, providing basic shapes whose
    properties can be set according to backing data. Mark property definitions may be simple constants or data
    fields, or scales can be used to map data values to visual values.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "marks",
                "any_of": [
                    {"range": "BaseRasterImageMark"},
                    {"range": "BaseRasterLabelMark"},
                    {"range": "BasePointsMark"},
                    {"range": "BaseShapesMark"},
                    {"range": "TextMark"},
                    {"range": "BaseGroupMark"},
                ],
                "domain_of": ["BaseGroupMark", "BaseViewConfiguration"],
            }
        },
    )

