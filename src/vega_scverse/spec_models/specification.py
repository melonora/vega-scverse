from typing import Optional

from .linkml_specification import BaseViewConfiguration
from pydantic import Field

from .scales import AxisScale, CategoricalColorScale
from .linkml_scales import LinearColorScale


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

