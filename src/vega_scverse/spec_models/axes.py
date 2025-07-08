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
        "description": "Vega like specification for the axes used in view "
        "configurations for the scverse visualization ecosystem.",
        "id": "https://w3id.org/scverse/vega-scverse/axes",
        "imports": ["linkml:types", "misc", "slots"],
        "license": "BSD-3",
        "name": "vega-scverse-axes",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": "src\\vega_scverse\\schema\\axes.yaml",
        "title": "vega-scverse-axes",
    }
)


class FontStyleValues(str, Enum):
    """
        Possible font styles. These are all the possible css font styles. These include styles,
    weights, variants and stretch. In case of font weights (100-900), it represents a unitless numeric scale
    standardized in CSS to represent font weight.
    """

    normal = "normal"
    """
    Regular CSS font style with a font weight of 400.
    """
    italic = "italic"
    """
    A cursive CSS font style.
    """
    bold = "bold"
    """
    A font with a thicker stroke weight relative to a regular font used to emphasize the text. It has a font weight
    of 700.
    """
    number_100 = "100"
    """
    The thinnest font weight available for a given font family.
    """
    number_200 = "200"
    number_300 = "300"
    number_500 = "500"
    number_600 = "600"
    number_800 = "800"
    number_900 = "900"
    """
    The thickest font weight available for a given font family.
    """
    small_caps = "small-caps"
    """
    Uppercase letterforms designed at approximately the same height and weight as the font’s lowercase letters.
    """
    ultra_condensed = "ultra-condensed"
    """
    The most horizontally narrow font stretch. The visual representation of each character is narrowed to its most
    compressed form.
    """
    extra_condensed = "extra-condensed"
    condensed = "condensed"
    semi_condensed = "semi-condensed"
    semi_expanded = "semi-expanded"
    expanded = "expanded"
    extra_expanded = "extra-expanded"
    ultra_expanded = "ultra-expanded"
    """
    The most horizontally expanded font stretch. The visual representation of each character is expanded to its most
    expanded form.
    """


class FontWeightValues(str, Enum):
    """
        Possible font weight values. In case of font weights (100-900), it represents a unitless numeric scale
    standardized in CSS to represent font weight.
    """

    number_100 = "100"
    """
    The thinnest font weight available for a given font family.
    """
    number_200 = "200"
    number_300 = "300"
    number_400 = "400"
    number_500 = "500"
    number_600 = "600"
    number_700 = "700"
    number_800 = "800"
    number_900 = "900"
    """
    The thickest font weight available for a given font family.
    """
    bold = "bold"
    """
    Font with a font weight of 700.
    """
    normal = "normal"
    """
    Font with a font weight of 400.
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


class AxisOrientEnum(str, Enum):
    left = "left"
    """
    Place a y-axis along the left edge of the chart.
    """
    right = "right"
    """
    Place a y-axis along the right edge of the chart.
    """
    top = "top"
    """
    Place an x-axis along the top edge of the chart.
    """
    bottom = "bottom"
    """
    Place an x-axis along the bottom edge of the chart.
    """


class CapEnum(str, Enum):
    butt = "butt"
    """
    The line ends exactly at its endpoint, producing a flat, squared-off edge perpendicular to the path. 
    There is no extension beyond the endpoint.
    """
    round = "round"
    """
    The line ends with a semi-circular extension beyond its endpoint, creating a rounded cap with a radius equal to 
    half the line’s thickness. This softens sharp edges and creates smooth joins.
    """
    square = "square"
    """
    The line ends with a square extension beyond its endpoint. It is similar to butt but extends the line slightly 
    past the endpoint, by half the line’s thickness, resulting in a squared-off cap that projects outward.
    """


class RGBHexItem(ConfiguredBaseModel):
    """
    RGB value represented by a hexadecimal string value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "value", "domain_of": ["RGBHexItem", "CircleShape"], "slot_uri": "rgbHexSlot"}
        },
    )


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
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "Axis"]}},
    )
    field: str = Field(
        default=...,
        description="""The value or field to which to apply the color.""",
        json_schema_extra={"linkml_meta": {"alias": "field", "domain_of": ["ColorItem", "AxisItem"]}},
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
                "domain_of": ["RGBHexItem", "CircleShape"],
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
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "Axis"]}},
    )
    field: AxisEnum = Field(
        default=...,
        description="""The mark's field value transformed by the scale. Either x or y.""",
        json_schema_extra={"linkml_meta": {"alias": "field", "domain_of": ["ColorItem", "AxisItem"]}},
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


class Axis(ConfiguredBaseModel):
    """
    An axis visualizes a spatial scale mapping for cartesian coordinates using ticks, grid lines and labels.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/axes"})

    scale: str = Field(
        default=...,
        description="""Name of the 'AxisScale' to visualize as axis object.""",
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "Axis"]}},
    )
    orient: AxisOrientEnum = Field(
        default=...,
        description="""The orientation of the axis, either 'left', 'right', 'top' or 'bottom'.""",
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Axis"]}},
    )
    domain: bool = Field(
        default=...,
        description="""A boolean flag indicating if the domain (the axis baseline, the line that the ticks connect to) should be 
included as part of the axis.""",
        json_schema_extra={"linkml_meta": {"alias": "domain", "domain_of": ["Axis"]}},
    )
    domainOpacity: Optional[str] = Field(
        default=None,
        description="""Opacity of axis domain line.""",
        json_schema_extra={
            "linkml_meta": {"alias": "domainOpacity", "domain_of": ["Axis"], "slot_uri": "opacityValueSlot"}
        },
    )
    domainColor: Optional[str] = Field(
        default=None,
        description="""Color of axis domain line.""",
        json_schema_extra={"linkml_meta": {"alias": "domainColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    domainWidth: Optional[float] = Field(
        default=None,
        description="""Stroke width of axis domain line.""",
        json_schema_extra={"linkml_meta": {"alias": "domainWidth", "domain_of": ["Axis"]}},
    )
    grid: Optional[bool] = Field(
        default=False,
        description="""A boolean flag indicating if grid lines should be included as part of the axis.""",
        json_schema_extra={"linkml_meta": {"alias": "grid", "domain_of": ["Axis"], "ifabsent": "False"}},
    )
    gridOpacity: Optional[str] = Field(
        default=None,
        description="""Opacity of axis grid lines.""",
        json_schema_extra={
            "linkml_meta": {"alias": "gridOpacity", "domain_of": ["Axis"], "slot_uri": "opacityValueSlot"}
        },
    )
    gridCap: Optional[CapEnum] = Field(
        default=None,
        description="""The stroke cap for axis grid lines. One of 'butt' (default), 'round' or 'square'.""",
        json_schema_extra={"linkml_meta": {"alias": "gridCap", "domain_of": ["Axis"]}},
    )
    gridColor: Optional[str] = Field(
        default=None,
        description="""Color of axis grid lines.""",
        json_schema_extra={"linkml_meta": {"alias": "gridColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    gridWidth: Optional[float] = Field(
        default=None,
        description="""Stroke width of axis grid lines.""",
        json_schema_extra={"linkml_meta": {"alias": "gridWidth", "domain_of": ["Axis"]}},
    )
    labelColor: Optional[str] = Field(
        default=None,
        description="""Text color of axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    labelOpacity: Optional[str] = Field(
        default=None,
        description="""Opacity of axis tick labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Axis"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default=None,
        description="""Font name for axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFont", "domain_of": ["Axis"]}},
    )
    labelFontSize: Optional[float] = Field(
        default=None,
        description="""Font size of axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Axis"]}},
    )
    labelFontStyle: Optional[str] = Field(
        default=None,
        description="""Font style of axis tick labels""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Axis"], "slot_uri": "FontStyleValues"}
        },
    )
    labelFontWeight: Optional[str] = Field(
        default=None,
        description="""Font weight of axis tick labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Axis"], "slot_uri": "FontWeightValues"}
        },
    )
    ticks: Optional[bool] = Field(
        default=True,
        description="""A boolean flag indicating if ticks should be included as part of the axis.""",
        json_schema_extra={"linkml_meta": {"alias": "ticks", "domain_of": ["Axis"], "ifabsent": "True"}},
    )
    tickOpacity: Optional[str] = Field(
        default=None,
        description="""Opacity of axis ticks.""",
        json_schema_extra={
            "linkml_meta": {"alias": "tickOpacity", "domain_of": ["Axis"], "slot_uri": "opacityValueSlot"}
        },
    )
    tickColor: Optional[str] = Field(
        default=None,
        description="""Color of axis ticks.""",
        json_schema_extra={"linkml_meta": {"alias": "tickColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    tickCap: Optional[CapEnum] = Field(
        default=None,
        description="""The stroke cap for axis tick marks. One of \"butt\" (default), \"round\" or \"square\".""",
        json_schema_extra={"linkml_meta": {"alias": "tickCap", "domain_of": ["Axis"]}},
    )
    tickWidth: Optional[str] = Field(
        default=None,
        description="""Width in pixels of axis ticks.""",
        json_schema_extra={
            "linkml_meta": {"alias": "tickWidth", "domain_of": ["Axis"], "slot_uri": "nonNegativeFloatSlot"}
        },
    )
    tickSize: Optional[str] = Field(
        default=None,
        description="""The length in pixels of axis ticks.""",
        json_schema_extra={
            "linkml_meta": {"alias": "tickSize", "domain_of": ["Axis"], "slot_uri": "nonNegativeFloatSlot"}
        },
    )
    values: list[Union[float, int]] = Field(
        default=...,
        description="""Explicitly set the visible axis tick and label values. The array entries should be legal values in the 
backing scale domain.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "values",
                "any_of": [{"range": "float"}, {"range": "integer"}],
                "domain_of": ["Axis"],
            }
        },
    )
    zindex: float = Field(
        default=...,
        description="""The integer z-index indicating the layering of the axis group relative to other axis, mark, and legend groups. 
The default value is 0 and axes and grid lines are drawn behind any marks defined in the same specification 
level. Higher values (1) will cause axes and grid lines to be drawn on top of marks.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis"]}},
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


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
RGBHexItem.model_rebuild()
RandomRGBSignal.model_rebuild()
ColorItem.model_rebuild()
CircleShape.model_rebuild()
AxisItem.model_rebuild()
Axis.model_rebuild()

