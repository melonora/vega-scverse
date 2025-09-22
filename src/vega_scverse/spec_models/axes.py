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


class FontStyleEnum(str, Enum):
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
    Uppercase letterforms designed at approximately the same height and weight as the font's lowercase letters.
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


class FontWeightEnum(str, Enum):
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
    """
    Possible values for the type of
    """

    x = "x"
    """
    x-axis of the visualization. Typically referring to the horizontal axis.
    """
    y = "y"
    """
    y-axis of the visualization. Typically referring to the vertical axis.
    """


class OrientEnum(str, Enum):
    """
    The position relative to the chart for either a (sub)title or axis.
    """

    left = "left"
    """
    Place a y-axis or title along the left side of the chart.
    """
    right = "right"
    """
    Place a y-axis or title along the right side of the chart.
    """
    top = "top"
    """
    Place an x-axis or title along the top side of the chart.
    """
    bottom = "bottom"
    """
    Place an x-axis or title along the bottom side of the chart.
    """


class BaseLineEnum(str, Enum):
    """
        The possible vertical alignments of the text relative to its y-coordinate.
    See the link for an explanation of the meaning of EM square. We do not currently
    support "line-bottom" and "line-top".
    """

    top = "top"
    """
    The highest part of all characters aligns with the y-coordinate.
    """
    middle = "middle"
    """
    The middle of the fonts EM square aligns with the y-coordinate.
    """
    bottom = "bottom"
    """
    The bottom of all characters combined aligns with the y-coordinate.
    """
    alphabetic = "alphabetic"
    """
    aligns the main body of lowercase letters (like a, e, x) so that their base sits exactly on the anchor line 
    (y coordinate). Descenders on letters like g, p, or y extend below this line.
    """


class HorizontalAlignEnum(str, Enum):
    """
    The horizontal text alignment relative to the anchor point of the text. One of left, center, or right.
    """

    left = "left"
    """
    The anchor point of the text is left of the text.
    """
    center = "center"
    """
    The anchor point of the text is at the center of the text.
    """
    right = "right"
    """
    The anchor point of the text is right of the text.
    """


class CapEnum(str, Enum):
    """
    The style of the stroke end for axis tick marks.
    """

    butt = "butt"
    """
    The line ends exactly at its endpoint, producing a flat, squared-off edge perpendicular to the path. 
    There is no extension beyond the endpoint.
    """
    round = "round"
    """
    The line ends with a semi-circular extension beyond its endpoint, creating a rounded cap with a radius equal to 
    half the line's thickness. This softens sharp edges and creates smooth joins.
    """
    square = "square"
    """
    The line ends with a square extension beyond its endpoint. It is similar to butt but extends the line slightly 
    past the endpoint, by half the line's thickness, resulting in a squared-off cap that projects outward.
    """


class PositionItem(ConfiguredBaseModel):
    """
    X or y position of an item in pixels.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: float = Field(
        default=...,
        description="""The coordinate value.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class TextItem(ConfiguredBaseModel):
    """
    Text to be displayed. Value is an array where each element corresponds to 1 line.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: list[str] = Field(
        default=...,
        description="""The value for text.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class BaselineItem(ConfiguredBaseModel):
    """
    The  vertical alignment of the text relative to its y-coordinate.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: BaseLineEnum = Field(
        default=...,
        description="""The value for the text baseline.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class FontItem(ConfiguredBaseModel):
    """
    The  name of the font to be used.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: str = Field(
        default=...,
        description="""The value for font name.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class FontSizeItem(ConfiguredBaseModel):
    """
    Fontsize in pixels of text.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: str = Field(
        default=...,
        description="""Font size value.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
                "slot_uri": "nonNegativeFloatSlot",
            }
        },
    )


class FontWeightItem(ConfiguredBaseModel):
    """
    Font weight of the text
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: FontWeightEnum = Field(
        default=...,
        description="""The font weight value.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class FontStyleItem(ConfiguredBaseModel):
    """
    Fontstyle of the text.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: FontStyleEnum = Field(
        default=...,
        description="""The fontstyle value.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class RGBHexItem(ConfiguredBaseModel):
    """
    RGB value represented by a hexadecimal string value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: Optional[str] = Field(
        default=None,
        description="""The RGB hex string value.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
                "slot_uri": "rgbHexSlot",
            }
        },
    )


class RandomRGBSignal(ConfiguredBaseModel):
    """
    RGB value represented by a hexadecimal string value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    signal: Optional[Literal["rgb(random()*255, random()*255, random()*255)"]] = Field(
        default="rgb",
        description="""Signal creating random RGB color for labels in a label raster.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "signal",
                "domain_of": ["RandomRGBSignal"],
                "equals_string": "rgb(random()*255, random()*255, random()*255)",
                "ifabsent": "string(rgb(random()*255, random()*255, random()*255))",
            }
        },
    )


class Title(ConfiguredBaseModel):
    """
    The title directive adds a descriptive title to a chart. Similar to scales, axes, and legends, a title can be
    defined at the top-level of a specification or as part of a group mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    text: list[str] = Field(
        default=...,
        description="""The title text. Either a string or an array of strings. The latter specifies multiple lines of text.""",
        json_schema_extra={"linkml_meta": {"alias": "text", "domain_of": ["Title"]}},
    )
    orient: OrientEnum = Field(
        default=...,
        description="""The orientation of the title relative to the chart.""",
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Title", "Axis"]}},
    )
    baseline: BaseLineEnum = Field(
        default=...,
        description="""The baseline attribute specifies the vertical alignment (baseline) of the text relative to its y-coordinate.""",
        json_schema_extra={"linkml_meta": {"alias": "baseline", "domain_of": ["Title"]}},
    )
    color: str = Field(
        default=...,
        description="""Text color of the title text.""",
        json_schema_extra={"linkml_meta": {"alias": "color", "domain_of": ["Title"], "slot_uri": "rgbaHexSlot"}},
    )
    font: str = Field(
        default=...,
        description="""Font name of the title text.""",
        json_schema_extra={"linkml_meta": {"alias": "font", "domain_of": ["Title"]}},
    )
    fontSize: float = Field(
        default=...,
        description="""Font size in pixels of the title text.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"alias": "fontSize", "domain_of": ["Title"]}},
    )
    fontStyle: FontStyleEnum = Field(
        default=...,
        description="""Fontstyle of the title.""",
        json_schema_extra={"linkml_meta": {"alias": "fontStyle", "domain_of": ["Title"]}},
    )
    fontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of the title""",
        json_schema_extra={"linkml_meta": {"alias": "fontWeight", "domain_of": ["Title"]}},
    )


class Padding(ConfiguredBaseModel):
    """
    padding defines the amount of space (in pixels) to reserve between the edge of the chart container and the inner
    view area where data marks are rendered. It acts as an internal margin that ensures visual elements like axes,
    titles, and legends don't touch or overflow the chart's outer boundaries.
    When combined with \"autosize\": {\"type\": \"fit\", \"contains\": \"padding\"}, this padding is included within the chart's
    specified width and height, and the inner view is resized accordingly to preserve layout integrity. If padding
    is defined with this class. This class should at least have one attribute defined.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    left: Optional[float] = Field(
        default=None,
        description="""The value for padding at the left side of the chart in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "left", "domain_of": ["Padding"]}},
    )
    top: Optional[float] = Field(
        default=None,
        description="""The value for padding at the top side of the chart in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "top", "domain_of": ["Padding"]}},
    )
    right: Optional[float] = Field(
        default=None,
        description="""The value for padding at the right side of the chart in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "right", "domain_of": ["Padding"]}},
    )
    bottom: Optional[float] = Field(
        default=None,
        description="""The value for padding at the bottom side of the chart in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "bottom", "domain_of": ["Padding"]}},
    )


class ColorItem(ConfiguredBaseModel):
    """
    A single color item definition specifying the scale on which the color is based and the value / field
    to which to apply the color.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

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


class PositiveFloatObject(ConfiguredBaseModel):
    """
    An object with an attribute value with a positive float as range. Useful for example to note the width of an
    outline.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: float = Field(
        default=...,
        description="""The actual width value in  pixels""",
        ge=0,
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


class CircleShapeObject(ConfiguredBaseModel):
    """
    Circle shape definition used in symbol mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: Optional[Literal["circle"]] = Field(
        default="circle",
        description="""Type of shape, in this case circle.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
                "equals_string": "circle",
                "ifabsent": "string(circle)",
            }
        },
    )


class AxisItem(ConfiguredBaseModel):
    """
    A axis item which for a mark can define the scale and field used for the axis definition in the mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

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


class OpacityObject(ConfiguredBaseModel):
    """
    The opacity for a given mark or label or other item to be rendered.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: float = Field(
        default=...,
        description="""The actual opacity value""",
        ge=0,
        le=1,
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "PositionItem",
                    "TextItem",
                    "baselineItem",
                    "FontItem",
                    "FontSizeItem",
                    "FontWeightItem",
                    "FontStyleItem",
                    "RGBHexItem",
                    "PositiveFloatObject",
                    "CircleShapeObject",
                    "OpacityObject",
                ],
            }
        },
    )


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
    orient: OrientEnum = Field(
        default=...,
        description="""The orientation of the axis, either 'left', 'right', 'top' or 'bottom'.""",
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Title", "Axis"]}},
    )
    domain: bool = Field(
        default=...,
        description="""A boolean flag indicating if the domain (the axis baseline, the line that the ticks connect to) should be 
included as part of the axis.""",
        json_schema_extra={"linkml_meta": {"alias": "domain", "domain_of": ["Axis"]}},
    )
    domainOpacity: Optional[float] = Field(
        default=None,
        description="""Opacity of axis domain line. Should not be present if domain is 'false'.""",
        ge=0,
        le=1,
        json_schema_extra={"linkml_meta": {"alias": "domainOpacity", "domain_of": ["Axis"]}},
    )
    domainColor: Optional[str] = Field(
        default=None,
        description="""Color of axis domain line. Should not be present if domain is 'false'.""",
        json_schema_extra={"linkml_meta": {"alias": "domainColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    domainWidth: Optional[float] = Field(
        default=None,
        description="""Stroke width of axis domain line. Should not be present if domain is 'false'.""",
        json_schema_extra={"linkml_meta": {"alias": "domainWidth", "domain_of": ["Axis"]}},
    )
    grid: Optional[bool] = Field(
        default=False,
        description="""A boolean flag indicating if grid lines should be included as part of the axis.""",
        json_schema_extra={"linkml_meta": {"alias": "grid", "domain_of": ["Axis"], "ifabsent": "False"}},
    )
    gridOpacity: Optional[float] = Field(
        default=None,
        description="""Opacity of axis grid lines. Should not be present if grid is 'false'.""",
        ge=0,
        le=1,
        json_schema_extra={"linkml_meta": {"alias": "gridOpacity", "domain_of": ["Axis"]}},
    )
    gridCap: Optional[CapEnum] = Field(
        default=None,
        description="""The stroke cap for axis grid lines. One of 'butt' (default), 'round' or 'square'.
Should not be present if grid is 'false'.""",
        json_schema_extra={"linkml_meta": {"alias": "gridCap", "domain_of": ["Axis"]}},
    )
    gridColor: Optional[str] = Field(
        default=None,
        description="""Color of axis grid lines. Should not be present if grid is 'false'.""",
        json_schema_extra={"linkml_meta": {"alias": "gridColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    gridWidth: Optional[float] = Field(
        default=None,
        description="""Stroke width of axis grid lines. Should not be present if grid is 'false'.""",
        json_schema_extra={"linkml_meta": {"alias": "gridWidth", "domain_of": ["Axis"]}},
    )
    labelColor: Optional[str] = Field(
        default=None,
        description="""Text color of axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelColor", "domain_of": ["Axis"], "slot_uri": "rgbHexSlot"}},
    )
    labelOpacity: Optional[float] = Field(
        default=None,
        description="""Opacity of axis tick labels.""",
        ge=0,
        le=1,
        json_schema_extra={"linkml_meta": {"alias": "labelOpacity", "domain_of": ["Axis"]}},
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
    labelFontStyle: Optional[FontStyleEnum] = Field(
        default=None,
        description="""Font style of axis tick labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Axis"]}},
    )
    labelFontWeight: Optional[FontWeightEnum] = Field(
        default=None,
        description="""Font weight of axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Axis"]}},
    )
    ticks: Optional[bool] = Field(
        default=True,
        description="""A boolean flag indicating if ticks should be included as part of the axis.""",
        json_schema_extra={"linkml_meta": {"alias": "ticks", "domain_of": ["Axis"], "ifabsent": "True"}},
    )
    tickOpacity: Optional[float] = Field(
        default=None,
        description="""Opacity of axis ticks.""",
        ge=0,
        le=1,
        json_schema_extra={"linkml_meta": {"alias": "tickOpacity", "domain_of": ["Axis"]}},
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
    tickWidth: Optional[float] = Field(
        default=None,
        description="""Width in pixels of axis ticks.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"alias": "tickWidth", "domain_of": ["Axis"]}},
    )
    tickSize: Optional[float] = Field(
        default=None,
        description="""The length in pixels of axis ticks.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"alias": "tickSize", "domain_of": ["Axis"]}},
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
PositionItem.model_rebuild()
TextItem.model_rebuild()
BaselineItem.model_rebuild()
FontItem.model_rebuild()
FontSizeItem.model_rebuild()
FontWeightItem.model_rebuild()
FontStyleItem.model_rebuild()
RGBHexItem.model_rebuild()
RandomRGBSignal.model_rebuild()
Title.model_rebuild()
Padding.model_rebuild()
ColorItem.model_rebuild()
PositiveFloatObject.model_rebuild()
CircleShapeObject.model_rebuild()
AxisItem.model_rebuild()
OpacityObject.model_rebuild()
Axis.model_rebuild()

