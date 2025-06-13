from __future__ import annotations

import re
import sys
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


metamodel_version = "None"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "created_by": "orcid:0000-0003-1666-5421",
        "default_prefix": "vega_scverse",
        "default_range": "string",
        "description": "Vega like specification for the scverse plotting ecosystem.",
        "id": "https://w3id.org/scverse/vega-scverse",
        "imports": ["linkml:types"],
        "license": "BSD-3",
        "name": "vega-scverse-scales",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": "scales.yaml",
        "title": "vega-scverse-scales",
    }
)


class ScaleEnum(str, Enum):
    linear = "linear"
    """
    Maps continuous numeric data to a continuous range.
    """
    ordinal = "ordinal"
    """
    Maps discrete values (categories) to distinct values in the output range.
    """


class AxisRangeEnum(str, Enum):
    height = "height"
    """
    Referring to the height of the plotting area.
    """
    width = "width"
    """
    Referring to the width of the plotting area.
    """


class Scales(ConfiguredBaseModel):
    """
    Vega like definition for scales which specifies a collection of mappings from a data domain  (e.g., numbers, categories, dates) to a visual range (e.g., position on the screen, color spectrum, size).

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse"})

    scales: Optional[list[str]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "scales",
                "any_of": [
                    {"range": "AxisScale"},
                    {"range": "CategoricalColorScale"},
                    {"range": "ContinuousColorScale"},
                ],
                "domain_of": ["Scales"],
            }
        },
    )


class Scale(ConfiguredBaseModel):
    """
    Base class for vega like scales which map from a data domain to a visual range, be it axis or color.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse"}
    )

    name: str = Field(
        default=...,
        description="""Name of the scale. Is used to refer to the scale in the rest of the view configuration. For scales used for axes typically `Y_scale` or `X_scale` optionally followed by `_n` where n stands for the index of the subplot. In case of a color mapping it is `color_` followed by a pseudo UUID.
""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and  visual range, e.g. `linear`.
""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Scale"]}},
    )


class AxisScale(Scale):
    """
    A vega like scale specifically for mapping from a data domain to an axis range.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse",
            "slot_usage": {
                "name": {
                    "description": "`Y_scale` or `X_scale` optionally "
                    "followed by `_n` where n stands for "
                    "the index of the subplot.\n",
                    "name": "name",
                    "pattern": "^[XY]_scale(_\\d+)?$",
                },
                "type": {
                    "description": "Only linear is supported for an " "`AxisScale` for now.",
                    "equals_string": "linear",
                    "ifabsent": "string(linear)",
                    "name": "type",
                },
            },
        }
    )

    domain: Optional[list[float]] = Field(
        default=None,
        description="""The set of input data values that the scale maps from. In the case of a linear scale, this should be a two-element list representing the minimum and maximum numeric values to be transformed. For example, [512.0, 0.0] maps the data range from 512 (top) to 0 (bottom), which is typical for Y-axis scales in image coordinate systems where the origin is at the top-left.
""",
        min_length=2,
        max_length=2,
        json_schema_extra={"linkml_meta": {"alias": "domain", "domain_of": ["AxisScale"]}},
    )
    range: Optional[AxisRangeEnum] = Field(
        default=None,
        description="""Defines the target visual dimension for the axis scaleÆs output range. Must be either 'width' for an X-axis  scale or 'height' for a Y-axis scale. These keywords refer to the pixel extent of the plotting area, not the  full canvas. The plotting area is the region where data marks are rendered, and its dimensions are typically  defined by the top-level 'width' and 'height' properties of a Vega specification. For example, setting  \"range\": \"height\" in a Y-axis scale maps the scaleÆs domain to pixel positions from top to bottom within the  plot area. This is commonly used to align data values with positional axes in coordinate-based visualizations.
""",
        json_schema_extra={"linkml_meta": {"alias": "range", "domain_of": ["AxisScale"]}},
    )
    name: str = Field(
        default=...,
        description="""`Y_scale` or `X_scale` optionally followed by `_n` where n stands for the index of the subplot.
""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: Literal["linear"] = Field(
        default="linear",
        description="""Only linear is supported for an `AxisScale` for now.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale"],
                "equals_string": "linear",
                "ifabsent": "string(linear)",
            }
        },
    )

    @field_validator("name")
    def pattern_name(cls, v):
        pattern = re.compile(r"^[XY]_scale(_\d+)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class ContinuousColorScale(Scale):
    """
    A vega like scale specifically for mapping from a data domain to an axis range.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse",
            "slot_usage": {
                "name": {
                    "description": "'Y_scale' or 'X_scale' optionally "
                    "followed by '_n' where n stands for "
                    "the index of the subplot\n",
                    "name": "name",
                    "pattern": "^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                }
            },
        }
    )

    name: str = Field(
        default=...,
        description="""'Y_scale' or 'X_scale' optionally followed by '_n' where n stands for the index of the subplot
""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and  visual range, e.g. `linear`.
""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Scale"]}},
    )

    @field_validator("name")
    def pattern_name(cls, v):
        pattern = re.compile(r"^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class CategoricalColorScale(Scale):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse"})

    name: str = Field(
        default=...,
        description="""Name of the scale. Is used to refer to the scale in the rest of the view configuration. For scales used for axes typically `Y_scale` or `X_scale` optionally followed by `_n` where n stands for the index of the subplot. In case of a color mapping it is `color_` followed by a pseudo UUID.
""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and  visual range, e.g. `linear`.
""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Scale"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Scales.model_rebuild()
Scale.model_rebuild()
AxisScale.model_rebuild()
ContinuousColorScale.model_rebuild()
CategoricalColorScale.model_rebuild()

