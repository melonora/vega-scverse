from .linkml_marks import BaseGroupMark, BaseRasterImageMark, BaseRasterLabelMark, BaseShapesMark, BasePointsMark, MarkDataSource
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