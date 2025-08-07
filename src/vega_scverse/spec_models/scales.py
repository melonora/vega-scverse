from typing import Annotated
from pydantic import Field, field_validator, model_validator

from .linkml_scales import BaseScales, BaseAxisScale, BaseCategoricalColorScale, LinearColorScale


class AxisScale(BaseAxisScale):
    @field_validator("domain")
    def domain_length(cls, v):
        if (length := len(v)) != 2:
            err_msg = f"AxisScale domain must be of length 2, but is of length: {length} "
            raise ValueError(err_msg)
        return v


class CategoricalColorScale(BaseCategoricalColorScale):
    @model_validator(mode="after")
    def check_domain_range_length(self) -> BaseCategoricalColorScale:
        if len(self.domain) != len(self.range):
            raise ValueError(
                f"`domain` and `range` must be of equal length, got {len(self.domain)} != {len(self.range)}")
        return self


class Scales(BaseScales):
    scales: Annotated[
        list[BaseAxisScale | BaseCategoricalColorScale | LinearColorScale],
        Field(
            json_schema_extra={
                "linkml_meta": {
                    "alias": "scales",
                    "any_of": [
                        {"range": "AxisScale"},
                        {"range": "CategoricalColorScale"},
                        {"range": "ContinuousColorScale"},
                    ],
                    "domain_of": ["ConcreteScales"],
                }
            }
        )
    ]

