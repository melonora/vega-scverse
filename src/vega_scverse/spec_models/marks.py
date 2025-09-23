from .linkml_marks import BaseGroupMark
from pydantic import Field

from .scales import AxisScale, CategoricalColorScale
from .linkml_scales import LinearColorScale


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