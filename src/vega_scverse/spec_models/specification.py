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
        "created_on": "2025-06-01T00:00:00",
        "default_prefix": "vega_scverse",
        "default_range": "string",
        "description": "The configuration entailing all the specification components "
        "for visualization of data in the scverse ecosystem.",
        "id": "https://w3id.org/scverse/vega-scverse/specification",
        "imports": ["linkml:types", "scales", "marks"],
        "license": "BSD-3",
        "name": "vega-scverse-specification",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": ".\\src\\vega_scverse\\schema\\specification.yaml",
        "title": "vega-scverse-specification",
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


class AxisEnum(str, Enum):
    x = "x"
    """
    x-axis of the visualization. Typically referring to the horizontal axis.
    """
    y = "y"
    """
    y-axis of the visualization. Typically referring to the vertical axis.
    """


class MarkTypeEnum(str, Enum):
    """
    The valid mark types within the scverse plotting / visualization ecosystem.
    """

    raster_image = "raster_image"
    """
    Mark used for a SpatialData image element.
    """
    raster_label = "raster_label"
    """
    Mark used for SpatialData label element.
    """
    symbol = "symbol"
    """
    The mark used for points data.
    """
    path = "path"
    """
    The mark used for circle and shapes geometries.
    """


class Scales(ConfiguredBaseModel):
    """
    Vega like definition for scales which specifies a collection of mappings from a data domain
    (e.g., numbers, categories, dates) to a visual range (e.g., position on the screen, color spectrum, size).
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/scales"})

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
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/scales"}
    )

    name: str = Field(
        default=...,
        description="""Name of the scale. Is used to refer to the scale in the rest of the view configuration. For scales used for
axes typically `Y_scale` or `X_scale` optionally followed by `_n` where n stands for the index of the subplot.
In case of a color mapping it is `color_` followed by a pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and 
visual range, e.g. `linear`.""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Scale", "Mark"]}},
    )


class AxisScale(Scale):
    """
    A vega like scale specifically for mapping from a data domain to an axis range.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/scales",
            "slot_usage": {
                "name": {
                    "description": "`Y_scale` or `X_scale` optionally "
                    "followed by `_n` where n stands for "
                    "the index of the subplot.",
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

    domain: list[float] = Field(
        default=...,
        description="""The set of input data values that the scale maps from. In the case of a linear scale,
this should be a two-element list representing the minimum and maximum numeric values
to be transformed. For example, [512.0, 0.0] maps the data range from 512 (top) to 0 (bottom),
which is typical for Y-axis scales in image coordinate systems where the origin is at the top-left.""",
        min_length=2,
        max_length=2,
        json_schema_extra={
            "linkml_meta": {
                "alias": "domain",
                "domain_of": ["AxisScale", "ContinuousColorScale", "CategoricalColorScale"],
            }
        },
    )
    range: AxisRangeEnum = Field(
        default=...,
        description="""Defines the target visual dimension for the axis scaleÆs output range. Must be either 'width' for an X-axis 
scale or 'height' for a Y-axis scale. These keywords refer to the pixel extent of the plotting area, not the 
full canvas. The plotting area is the region where data marks are rendered, and its dimensions are typically 
defined by the top-level 'width' and 'height' properties of a Vega specification. For example, setting 
\"range\": \"height\" in a Y-axis scale maps the scaleÆs domain to pixel positions from top to bottom within the 
plot area. This is commonly used to align data values with positional axes in coordinate-based visualizations.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "range",
                "domain_of": ["AxisScale", "ContinuousColorScale", "CategoricalColorScale"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""`Y_scale` or `X_scale` optionally followed by `_n` where n stands for the index of the subplot.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: Literal["linear"] = Field(
        default="linear",
        description="""Only linear is supported for an `AxisScale` for now.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
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


class ColorScale(Scale):
    """
    Abstract class to map a data domain to a color range. Not to be used on its own.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "from_schema": "https://w3id.org/scverse/vega-scverse/scales",
            "slot_usage": {
                "name": {
                    "description": "color followed by '_pseudoUUID' used "
                    "to refer to this scale elsewhere in "
                    "the view configuration.",
                    "name": "name",
                    "pattern": "^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                }
            },
        }
    )

    name: str = Field(
        default=...,
        description="""color followed by '_pseudoUUID' used to refer to this scale elsewhere in the view configuration.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and 
visual range, e.g. `linear`.""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Scale", "Mark"]}},
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


class ContinuousColorScale(ColorScale):
    """
    A vega like scale specifically for mapping from a continuous data domain to a visual color range.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/scales",
            "slot_usage": {
                "type": {
                    "description": "Only linear is supported for an " "`ContinuousColorScale` for now.",
                    "equals_string": "linear",
                    "ifabsent": "string(linear)",
                    "name": "type",
                }
            },
        }
    )

    domain: ContinuousColorDomain = Field(
        default=...,
        description="""The data used as a source for the visual color range""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "domain",
                "domain_of": ["AxisScale", "ContinuousColorScale", "CategoricalColorScale"],
            }
        },
    )
    range: ContinuousColorMapRange = Field(
        default=...,
        description="""The range to which to map the data domain. In this case one that refers to a colormap range.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "range",
                "domain_of": ["AxisScale", "ContinuousColorScale", "CategoricalColorScale"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""color followed by '_pseudoUUID' used to refer to this scale elsewhere in the view configuration.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: Literal["linear"] = Field(
        default="linear",
        description="""Only linear is supported for an `ContinuousColorScale` for now.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
                "equals_string": "linear",
                "ifabsent": "string(linear)",
            }
        },
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


class CategoricalColorScale(ColorScale):
    """
    A scale to map a discrete data domain to discrete colors
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/scales",
            "slot_usage": {"type": {"equals_string": "ordinal", "ifabsent": "string(ordinal)", "name": "type"}},
        }
    )

    domain: list[str] = Field(
        default=...,
        description="""The data domain as a list of discrete string values.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "domain",
                "domain_of": ["AxisScale", "ContinuousColorScale", "CategoricalColorScale"],
            }
        },
    )
    range: list[str] = Field(
        default=...,
        description="""List of RGB colors as hexadecimal strings""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "range",
                "domain_of": ["AxisScale", "ContinuousColorScale", "CategoricalColorScale"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""color followed by '_pseudoUUID' used to refer to this scale elsewhere in the view configuration.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Scale"]}},
    )
    type: Literal["ordinal"] = Field(
        default="ordinal",
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and 
visual range, e.g. `linear`.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
                "equals_string": "ordinal",
                "ifabsent": "string(ordinal)",
            }
        },
    )

    @field_validator("range")
    def pattern_range(cls, v):
        pattern = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid range format: {v}"
            raise ValueError(err_msg)
        return v

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


class ContinuousColorDomain(ConfiguredBaseModel):
    """
    A data domain or source for a ContinuousColorScale.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/scales"})

    data: str = Field(
        default=...,
        description="""The identifier of the particular data object in the data array to which the color mapping in 
ContinuousColorScale must be applied. In Vega this is only defined when the type of Scale is
ordinal, but we deviate from that.""",
        json_schema_extra={"linkml_meta": {"alias": "data", "domain_of": ["ContinuousColorDomain", "MarkDataSource"]}},
    )
    field: str = Field(
        default=...,
        description="""If the data source is a table, then the field is the column within the table that is used as 
a source for the color mapping. In case of raster data with a single channel, the field equals
\"value\" and if multichannel raster data it is the name or index of the image channel.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": ["ContinuousColorDomain", "ColorItem", "AxisItem", "ConditionalFillUpdate"],
            }
        },
    )

    @field_validator("data")
    def pattern_data(cls, v):
        pattern = re.compile(r"^.*_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid data format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid data format: {v}"
            raise ValueError(err_msg)
        return v


class ContinuousColorMapRange(ConfiguredBaseModel):
    """
    Color scheme reference for a color palette.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/scales"})

    scheme: str = Field(
        default=...,
        description="""The name of the color scheme to use or an array of color values.""",
        json_schema_extra={"linkml_meta": {"alias": "scheme", "domain_of": ["ContinuousColorMapRange"]}},
    )
    count: int = Field(
        default=...,
        description="""The number of colors to use in the scheme.""",
        json_schema_extra={"linkml_meta": {"alias": "count", "domain_of": ["ContinuousColorMapRange"]}},
    )


class Value(ConfiguredBaseModel):
    """
    Represents either a literal value or a signal-based dynamic value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/marks"}
    )

    value: Optional[float] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "CircleShape"]}},
    )


class OpacityValue(Value):
    """
    A numeric value representing the transparency level of a visual element, typically ranging from 0 to 1.
      - 0 means fully transparent (invisible).
      - 1 means fully opaque (no transparency).
      - Values in between represent varying levels of transparency.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/marks",
            "slot_usage": {"value": {"maximum_value": 1, "minimum_value": 0, "name": "value"}},
        }
    )

    value: Optional[float] = Field(
        default=None,
        ge=0,
        le=1,
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "CircleShape"]}},
    )


class PositiveValue(Value):
    """
    A value above 0.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/marks",
            "slot_usage": {"value": {"minimum_value": 0, "name": "value"}},
        }
    )

    value: Optional[float] = Field(
        default=None,
        ge=0,
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "CircleShape"]}},
    )


class RGBHex(ConfiguredBaseModel):
    """
    RGB value represented by a hexadecimal string value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "CircleShape"]}},
    )

    @field_validator("value")
    def pattern_value(cls, v):
        pattern = re.compile(r"^#([A-Fa-f0-9]{6})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid value format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid value format: {v}"
            raise ValueError(err_msg)
        return v


class RandomRGBSignal(ConfiguredBaseModel):
    """
    RGB value represented by a hexadecimal string value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    signal: Optional[Literal["rgb(random()*255, random()*255, random()*255)"]] = Field(
        default="rgb",
        json_schema_extra={
            "linkml_meta": {
                "alias": "signal",
                "domain_of": ["RandomRGBSignal"],
                "equals_string": "rgb(random()*255, random()*255, random()*255)",
                "ifabsent": "string(rgb(random()*255, random()*255, random()*255))",
            }
        },
    )


class ColorItem(ConfiguredBaseModel):
    """
    A single color item definition specifying the scale on which the color is based and the value / field
    to which to apply the color.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/slots"})

    scale: str = Field(
        default=...,
        description="""The color scale.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: str = Field(
        default=...,
        description="""The value or field to which to apply the color.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": ["ContinuousColorDomain", "ColorItem", "AxisItem", "ConditionalFillUpdate"],
            }
        },
    )

    @field_validator("scale")
    def pattern_scale(cls, v):
        pattern = re.compile(r"^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid scale format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid scale format: {v}"
            raise ValueError(err_msg)
        return v


class CircleShape(ConfiguredBaseModel):
    """
    Circle shape definition used in symbol mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/slots"})

    value: Optional[Literal["circle"]] = Field(
        default="circle",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": ["Value", "RGBHex", "CircleShape"],
                "equals_string": "circle",
                "ifabsent": "string(circle)",
            }
        },
    )


class AxisItem(ConfiguredBaseModel):
    """
    A axis item which for a mark can define the scale and field used for the axis definition in the mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/slots"})

    scale: str = Field(
        default=...,
        description="""The scale on which the axis is based.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: AxisEnum = Field(
        default=...,
        description="""The mark's field value transformed by the scale. Either x or y.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": ["ContinuousColorDomain", "ColorItem", "AxisItem", "ConditionalFillUpdate"],
            }
        },
    )

    @field_validator("scale")
    def pattern_scale(cls, v):
        pattern = re.compile(r"^[XY]_scale(_\d+)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid scale format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid scale format: {v}"
            raise ValueError(err_msg)
        return v


class ImageEncode(ConfiguredBaseModel):
    """
    A set of visual encoding properties that determine the position and appearance of a 'raster_image' mark.
    In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data
    is processed for the first time and a mark instance is newly added to a scene and are the only properties
    supported for a 'raster_image' mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    enter: ImageEncodeEnter = Field(
        default=...,
        description="""Enter properties that are evaluated when image data is processed for the first time and the raster_image mark 
is newly added to a scene.""",
        json_schema_extra={
            "linkml_meta": {"alias": "enter", "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )


class LabelEncode(ConfiguredBaseModel):
    """
    A set of visual encoding properties that determine the position and appearance of a 'raster_label' mark.
    In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data
    is processed for the first time and a mark instance is newly added to a scene. The update properties are evaluated
    for all existing (non-exiting) mark instances. The exit properties are evaluated when the data backing a mark is
    removed, and so the mark is leaving the visual scene. However, in this specification we currently only support
    enter and update property sets for a 'raster_label' mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    enter: LabelEncodeEnter = Field(
        default=...,
        description="""Enter properties that are evaluated when label data is processed for the first time and the raster_label mark 
is newly added to a scene.""",
        json_schema_extra={
            "linkml_meta": {"alias": "enter", "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )
    update: Optional[MarkEncodeUpdate] = Field(
        default=None,
        description="""Update properties that are evaluated for all existing (non-exiting) mark instances. Typically included when 
no random coloring is being used for the labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "update", "domain_of": ["LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )


class SymbolEncode(ConfiguredBaseModel):
    """
    A set of visual encoding properties that determine the position and appearance of a 'symbol' mark.
    In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data
    is processed for the first time and a mark instance is newly added to a scene. The update properties are evaluated
    for all existing (non-exiting) mark instances. The exit properties are evaluated when the data backing a mark is
    removed, and so the mark is leaving the visual scene. However, in this specification we currently only support
    enter and update property sets for a 'symbol' mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    enter: PointsEncodeEnter = Field(
        default=...,
        description="""Enter properties that are evaluated when points data is processed for the first time and the points mark 
is newly added to a scene.""",
        json_schema_extra={
            "linkml_meta": {"alias": "enter", "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )
    update: Optional[MarkEncodeUpdate] = Field(
        default=None,
        description="""Update properties that are evaluated for all existing (non-exiting) mark instances. Usually defined if the 
user specified a color to be used for the PointsMark.""",
        json_schema_extra={
            "linkml_meta": {"alias": "update", "domain_of": ["LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )


class PathEncode(ConfiguredBaseModel):
    """
    A set of visual encoding properties that determine the position and appearance of a 'path' mark.
    In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data
    is processed for the first time and a mark instance is newly added to a scene. The update properties are evaluated
    for all existing (non-exiting) mark instances. The exit properties are evaluated when the data backing a mark is
    removed, and so the mark is leaving the visual scene. However, in this specification we currently only support
    enter and update property sets for a 'path' mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    enter: PathEncodeEnter = Field(
        default=...,
        description="""Enter properties that are evaluated when points data is processed for the first time and the points mark 
is newly added to a scene.""",
        json_schema_extra={
            "linkml_meta": {"alias": "enter", "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )
    update: Optional[MarkEncodeUpdate] = Field(
        default=None,
        description="""Update properties that are evaluated for all existing (non-exiting) mark instances. Usually defined if the 
user specified a color to be used for the PointsMark.""",
        json_schema_extra={
            "linkml_meta": {"alias": "update", "domain_of": ["LabelEncode", "SymbolEncode", "PathEncode"]}
        },
    )


class ImageEncodeEnter(ConfiguredBaseModel):
    """
    Enter properties that are evaluated when image data is processed for the first time and the raster_image mark is
    newly added to a scene.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    opacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {"alias": "opacity", "domain_of": ["ImageEncodeEnter"], "slot_uri": "opacity"}
        },
    )
    fill: list[ColorItem] = Field(
        default=...,
        description="""The colormap by which to show the intensity value of the image or channel.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )


class LabelEncodeEnter(ConfiguredBaseModel):
    """
    Enter properties that are evaluated when label data is processed for the first time and the raster_image mark is
    newly added to a scene.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    stroke: list[ColorItem] = Field(
        default=...,
        description="""The color of the outline of each individual label.""",
        min_length=1,
        max_length=1,
        json_schema_extra={"linkml_meta": {"alias": "stroke", "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"]}},
    )
    fill: list[Union[ColorItem, RandomRGBSignal]] = Field(
        default=...,
        description="""The color fill of each individual label.""",
        min_length=1,
        max_length=1,
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ColorItem"}, {"range": "RandomRGBSignal"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )
    fillOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
                "slot_uri": "fillOpacity",
            }
        },
    )
    strokeOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
                "slot_uri": "strokeOpacity",
            }
        },
    )
    strokeWidth: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
                "slot_uri": "strokeWidth",
            }
        },
    )


class PointsEncodeEnter(ConfiguredBaseModel):
    """
    Enter properties that are evaluated when points data is processed for the first time and the raster_image mark is
    newly added to a scene.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    x: AxisItem = Field(
        default=...,
        description="""The x coordinates""",
        json_schema_extra={"linkml_meta": {"alias": "x", "domain_of": ["PointsEncodeEnter", "PathEncodeEnter"]}},
    )
    y: AxisItem = Field(
        default=...,
        description="""The y coordinates""",
        json_schema_extra={"linkml_meta": {"alias": "y", "domain_of": ["PointsEncodeEnter", "PathEncodeEnter"]}},
    )
    stroke: Union[ColorItem, RGBHex] = Field(
        default=...,
        description="""The color of the outline of each individual label.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "stroke",
                "any_of": [{"range": "ColorItem"}, {"range": "RGBHex"}],
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
            }
        },
    )
    fill: Union[ColorItem, RGBHex] = Field(
        default=...,
        description="""The color fill of each individual label.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ColorItem"}, {"range": "RGBHex"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )
    fillOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
                "slot_uri": "fillOpacity",
            }
        },
    )
    strokeOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
                "slot_uri": "strokeOpacity",
            }
        },
    )
    strokeWidth: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
                "slot_uri": "strokeWidth",
            }
        },
    )
    size: str = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "size", "domain_of": ["PointsEncodeEnter"], "slot_uri": "size"}},
    )
    shape: CircleShape = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "shape", "domain_of": ["PointsEncodeEnter"]}}
    )


class PathEncodeEnter(ConfiguredBaseModel):
    """
    Enter properties that are evaluated when shapes data is processed for the first time and the raster_image mark is
    newly added to a scene.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    x: AxisItem = Field(
        default=...,
        description="""The x coordinates""",
        json_schema_extra={"linkml_meta": {"alias": "x", "domain_of": ["PointsEncodeEnter", "PathEncodeEnter"]}},
    )
    y: AxisItem = Field(
        default=...,
        description="""The y coordinates""",
        json_schema_extra={"linkml_meta": {"alias": "y", "domain_of": ["PointsEncodeEnter", "PathEncodeEnter"]}},
    )
    fill: Union[ColorItem, RGBHex] = Field(
        default=...,
        description="""The color fill of each individual label.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ColorItem"}, {"range": "RGBHex"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )
    fillOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
                "slot_uri": "fillOpacity",
            }
        },
    )


class MarkEncodeUpdate(ConfiguredBaseModel):
    """
    Update properties that are evaluated for all existing (non-exiting) mark instances.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    fill: Optional[list[Union[ConditionalFillUpdate, RGBHex]]] = Field(
        default=None,
        description="""Update of fill color based on a test condition and optional a backup static fill value""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ConditionalFillUpdate"}, {"range": "RGBHex"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )


class ConditionalFillUpdate(ConfiguredBaseModel):
    """
    Update color based on test condition. This is following an 'if-then-else' style chain of production rules. If
    no else is specified, then the property value evaluates to 'null' or similar value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    test: str = Field(
        default=...,
        description="""The condition to test on, e.g. 'isValid(datum.value). MUST be a valid expression in Vega. See also:
https://vega.github.io/vega/docs/expressions/ and it MUST evaluate to either 'true' or 'false'.""",
        json_schema_extra={"linkml_meta": {"alias": "test", "domain_of": ["ConditionalFillUpdate"]}},
    )
    scale: str = Field(
        default=...,
        description="""The scale to use for applying the fill color. This scale MUST exist in the view configuration Scales array.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: str = Field(
        default=...,
        description="""The column that serves as data input, in the test condition this corresponds to 'datum'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": ["ContinuousColorDomain", "ColorItem", "AxisItem", "ConditionalFillUpdate"],
            }
        },
    )

    @field_validator("scale")
    def pattern_scale(cls, v):
        pattern = re.compile(r"^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid scale format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid scale format: {v}"
            raise ValueError(err_msg)
        return v


class Mark(ConfiguredBaseModel):
    """
    Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting symbols.
    Marks are the basic visual building block of a visualization, providing basic shapes whose properties can be set
    according to backing data. Mark property definitions may be simple constants or data fields, or scales can be
    used to map data values to visual values.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/marks"}
    )

    type: MarkTypeEnum = Field(
        default=...,
        description="""The type of mark.""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Scale", "Mark"]}},
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )
    encode: str = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of mark instances. In Vega, 
there are three primary property sets: enter, update, exit. The enter properties are evaluated when data is 
processed for the first time and a mark instance is newly added to a scene. The update properties are 
evaluated for all existing (non-exiting) mark instances. The exit properties are evaluated when the data 
backing a mark is removed, and so the mark is leaving the visual scene. However, in this specification we 
currently only support enter and update property sets.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Mark"]}},
    )


class MarkDataSource(ConfiguredBaseModel):
    """
    Object with a data field pointing to the name of the datastream that serves as data source for the mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    data: str = Field(
        default=...,
        description="""name of the datastream""",
        json_schema_extra={"linkml_meta": {"alias": "data", "domain_of": ["ContinuousColorDomain", "MarkDataSource"]}},
    )

    @field_validator("data")
    def pattern_data(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid data format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid data format: {v}"
            raise ValueError(err_msg)
        return v


class RasterImageMark(Mark):
    """
    Graphical mark encoding an image.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/marks",
            "slot_usage": {
                "encode": {
                    "description": "A set of visual encoding properties "
                    "that determine the position and "
                    "appearance of the raster_image "
                    "mark.",
                    "name": "encode",
                    "range": "ImageEncode",
                },
                "type": {
                    "description": "The type of the mark. In this case, " "it is always 'raster_image'",
                    "equals_string": "raster_image",
                    "ifabsent": "string(raster_image)",
                    "name": "type",
                },
            },
        }
    )

    type: Literal["raster_image"] = Field(
        default="raster_image",
        description="""The type of the mark. In this case, it is always 'raster_image'""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
                "equals_string": "raster_image",
                "ifabsent": "string(raster_image)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )
    encode: ImageEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the raster_image mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Mark"]}},
    )


class RasterLabelMark(Mark):
    """
    Graphical mark encoding a label image.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/marks",
            "slot_usage": {
                "encode": {
                    "description": "A set of visual encoding properties "
                    "that determine the position and "
                    "appearance of the raster_image "
                    "mark.",
                    "name": "encode",
                    "range": "LabelEncode",
                },
                "type": {
                    "description": "The type of the mark. In this case, " "it is always 'raster_label'",
                    "equals_string": "raster_label",
                    "ifabsent": "string(raster_label)",
                    "name": "type",
                },
            },
        }
    )

    type: Literal["raster_label"] = Field(
        default="raster_label",
        description="""The type of the mark. In this case, it is always 'raster_label'""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
                "equals_string": "raster_label",
                "ifabsent": "string(raster_label)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )
    encode: LabelEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the raster_image mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Mark"]}},
    )


class PointsMark(Mark):
    """
    Graphical mark for encoding points data, using a vega like symbol mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/marks",
            "slot_usage": {
                "encode": {
                    "description": "A set of visual encoding properties "
                    "that determine the position and "
                    "appearance of the symbol mark.",
                    "name": "encode",
                    "range": "SymbolEncode",
                },
                "type": {
                    "description": "The type of the mark. In this case, " "it is always 'symbol'.",
                    "equals_string": "symbol",
                    "ifabsent": "string(symbol)",
                    "name": "type",
                },
            },
        }
    )

    type: Literal["symbol"] = Field(
        default="symbol",
        description="""The type of the mark. In this case, it is always 'symbol'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
                "equals_string": "symbol",
                "ifabsent": "string(symbol)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )
    encode: SymbolEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the symbol mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Mark"]}},
    )


class ShapesMark(Mark):
    """
    Graphical mark for encoding shapes data, using a vega like path mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/marks",
            "slot_usage": {
                "encode": {
                    "description": "A set of visual encoding properties "
                    "that determine the position and "
                    "appearance of the symbol mark.",
                    "name": "encode",
                    "range": "PathEncode",
                },
                "type": {
                    "description": "The type of the mark. In this case, " "it is always 'symbol'.",
                    "equals_string": "path",
                    "ifabsent": "string(path)",
                    "name": "type",
                },
            },
        }
    )

    type: Literal["path"] = Field(
        default="path",
        description="""The type of the mark. In this case, it is always 'symbol'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Scale", "Mark"],
                "equals_string": "path",
                "ifabsent": "string(path)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["Mark"]}},
    )
    encode: PathEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the symbol mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Mark"]}},
    )


class Padding(ConfiguredBaseModel):
    """
    padding defines the amount of space (in pixels) to reserve between the edge of the chart container and the inner
    view area where data marks are rendered. It acts as an internal margin that ensures visual elements like axes,
    titles, and legends donÆt touch or overflow the chartÆs outer boundaries.
    When combined with \"autosize\": {\"type\": \"fit\", \"contains\": \"padding\"}, this padding is included within the chart's
    specified width and height, and the inner view is resized accordingly to preserve layout integrity. If padding
    is defined with this class. This class should at least have one attribute defined.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/scverse/vega-scverse/specification"}
    )

    left: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "left", "domain_of": ["Padding"]}}
    )
    top: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "top", "domain_of": ["Padding"]}}
    )
    right: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "right", "domain_of": ["Padding"]}}
    )
    bottom: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"alias": "bottom", "domain_of": ["Padding"]}}
    )


class ViewConfiguration(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/scverse/vega-scverse/specification"}
    )

    height: int = Field(
        default=...,
        description="""The height of the plotting area. The plotting area is defined as the rectangular region within a visualization 
where graphical marks (such as points, lines, or bars) are rendered, bounded by the axes and padding, 
excluding titles, legends, and margins.""",
        json_schema_extra={"linkml_meta": {"alias": "height", "domain_of": ["ViewConfiguration"]}},
    )
    width: int = Field(
        default=...,
        description="""The width of the plotting area. The plotting area is defined as the rectangular region within a visualization 
where graphical marks (such as points, lines, or bars) are rendered, bounded by the axes and padding, 
excluding titles, legends, and margins.""",
        json_schema_extra={"linkml_meta": {"alias": "width", "domain_of": ["ViewConfiguration"]}},
    )
    padding: Optional[Union[Padding, float]] = Field(
        default=None,
        description="""padding defines the amount of space (in pixels) to reserve between the edge of the chart container and the inner 
view area where data marks are rendered. It acts as an internal margin that ensures visual elements like axes, 
titles, and legends donÆt touch or overflow the chartÆs outer boundaries.
When combined with \"autosize\": {\"type\": \"fit\", \"contains\": \"padding\"}, this padding is included within the chart's 
specified width and height, and the inner view is resized accordingly to preserve layout integrity. If padding
is defined with this class. This class should at least have one attribute defined.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "padding",
                "any_of": [{"range": "float"}, {"range": "Padding"}],
                "domain_of": ["ViewConfiguration"],
            }
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""The title directive adds a descriptive title to a chart.""",
        json_schema_extra={"linkml_meta": {"alias": "title", "domain_of": ["ViewConfiguration"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Scales.model_rebuild()
Scale.model_rebuild()
AxisScale.model_rebuild()
ColorScale.model_rebuild()
ContinuousColorScale.model_rebuild()
CategoricalColorScale.model_rebuild()
ContinuousColorDomain.model_rebuild()
ContinuousColorMapRange.model_rebuild()
Value.model_rebuild()
OpacityValue.model_rebuild()
PositiveValue.model_rebuild()
RGBHex.model_rebuild()
RandomRGBSignal.model_rebuild()
ColorItem.model_rebuild()
CircleShape.model_rebuild()
AxisItem.model_rebuild()
ImageEncode.model_rebuild()
LabelEncode.model_rebuild()
SymbolEncode.model_rebuild()
PathEncode.model_rebuild()
ImageEncodeEnter.model_rebuild()
LabelEncodeEnter.model_rebuild()
PointsEncodeEnter.model_rebuild()
PathEncodeEnter.model_rebuild()
MarkEncodeUpdate.model_rebuild()
ConditionalFillUpdate.model_rebuild()
Mark.model_rebuild()
MarkDataSource.model_rebuild()
RasterImageMark.model_rebuild()
RasterLabelMark.model_rebuild()
PointsMark.model_rebuild()
ShapesMark.model_rebuild()
Padding.model_rebuild()
ViewConfiguration.model_rebuild()

