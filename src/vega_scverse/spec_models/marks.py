from typing import Union

from .linkml_marks import BaseGroupMark, BaseRasterImageMark, BaseRasterLabelMark, BaseShapesMark, BasePointsMark, \
    MarkDataSource, TextMark
from pydantic import Field

from .scales import AxisScale, CategoricalColorScale
from .linkml_scales import LinearColorScale


class RasterImageMark(BaseRasterImageMark):
    from_: MarkDataSource = Field(
        default=...,
        alias="from",
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )


class RasterLabelMark(BaseRasterLabelMark):
    from_: MarkDataSource = Field(
        default=...,
        alias="from",
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )


class PointsMark(BasePointsMark):
    from_: MarkDataSource = Field(
        default=...,
        alias="from",
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )


class ShapesMark(BaseShapesMark):
    from_: MarkDataSource = Field(
        default=...,
        alias="from",
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )


class GroupMark(BaseGroupMark):
    scales: list[AxisScale | CategoricalColorScale | LinearColorScale] = Field(
        default=...,
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
        Union[PointsMark, RasterImageMark, RasterLabelMark, ShapesMark, TextMark]
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