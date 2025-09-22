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
        "description": "Vega like specification for the legends used in view "
        "configurations for the scverse visualization ecosystem.",
        "id": "https://w3id.org/scverse/vega-scverse/legends",
        "imports": ["linkml:types", "slots", "misc"],
        "license": "BSD-3",
        "name": "vega-scverse-legends",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": "src\\vega_scverse\\schema\\legends.yaml",
        "title": "vega-scverse-legends",
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


class LegendType(str, Enum):
    """
    The valid mark types within the scverse plotting / visualization ecosystem.
    """

    discrete = "discrete"
    """
    legend type for categorical data
    """
    gradient = "gradient"
    """
    legend type for continuous data
    """


class LegendDirections(str, Enum):
    """
    The possible directions of the legend.
    """

    horizontal = "horizontal"
    """
    legend direction with the longest axis oriented along the horizontal axis.
    """
    vertical = "vertical"
    """
    legend direction with the longest axis oriented along the vertical axis.
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
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Title", "Legend"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem"]}},
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


class Legend(ConfiguredBaseModel):
    """
    Vega like configuration for specifying legends in the SpatialData visualization ecosystem.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/legends"}
    )

    type: LegendType = Field(
        default=...,
        description="""The type of legend, either 'gradient' (continuous data) or 'discrete' (categorical data).""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Legend"]}},
    )
    direction: LegendDirections = Field(
        default=...,
        description="""The direction of the legend, one of 'vertical' or 'horizontal'.""",
        json_schema_extra={"linkml_meta": {"alias": "direction", "domain_of": ["Legend"]}},
    )
    orient: Optional[Literal["none"]] = Field(
        default="none",
        description="""The orientation of the legend, determining where the legend is placed relative to a chart's data rectangle. 
Currently, only 'none' is allowed here as in Vega this allows to directly specify the positioning in 
pixel coordinates. If there is demand, this can be changed.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "orient",
                "domain_of": ["Title", "Legend"],
                "equals_string": "none",
                "ifabsent": "string(none)",
            }
        },
    )
    padding: Optional[float] = Field(
        default=None,
        description="""The padding between the border and content of the legend group in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "padding", "domain_of": ["Legend"]}},
    )
    fill: str = Field(
        default=...,
        description="""The name of a scale that maps to a fill color. This represents the color used to visualize discrete classes
or continuous data in the legend.""",
        json_schema_extra={"linkml_meta": {"alias": "fill", "domain_of": ["Legend"]}},
    )
    fillColor: Optional[str] = Field(
        default=None,
        description="""Hex string representing a RGBA color, which is the background color of the legend.""",
        json_schema_extra={"linkml_meta": {"alias": "fillColor", "domain_of": ["Legend"], "slot_uri": "rgbaHexSlot"}},
    )
    strokeColor: Optional[str] = Field(
        default=None,
        description="""Hex string representing a RGBA color, which is the color of the legend border.""",
        json_schema_extra={"linkml_meta": {"alias": "strokeColor", "domain_of": ["Legend"], "slot_uri": "rgbaHexSlot"}},
    )
    strokeWidth: Optional[float] = Field(
        default=None,
        description="""The width of the legend border in pixels. This property deviates from its Vega equivalent, in that the 
vega equivalent expects a 'Scale'.""",
        json_schema_extra={"linkml_meta": {"alias": "strokeWidth", "domain_of": ["Legend"]}},
    )
    labelOffset: float = Field(
        default=...,
        description="""Offset in pixels between legend labels their corresponding symbol or gradient.""",
        json_schema_extra={"linkml_meta": {"alias": "labelOffset", "domain_of": ["Legend"]}},
    )
    labelAlign: HorizontalAlignEnum = Field(
        default=...,
        description="""Horizontal text alignment for legend labels. In short this means where the label text is relative to the
anchor point of the labels (this could be defined as the coordinates where the labels are specified to be).""",
        json_schema_extra={"linkml_meta": {"alias": "labelAlign", "domain_of": ["Legend"]}},
    )
    labelColor: str = Field(
        default=...,
        description="""Text color for legend labels represented by a RGB hex string.""",
        json_schema_extra={"linkml_meta": {"alias": "labelColor", "domain_of": ["Legend"], "slot_uri": "rgbHexSlot"}},
    )
    labelOpacity: str = Field(
        default=...,
        description="""The opacity of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Legend"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default="Arial",
        description="""Font name for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFont", "domain_of": ["Legend"], "ifabsent": "string(Arial)"}},
    )
    labelFontSize: float = Field(
        default=...,
        description="""Font size in pixels for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Legend"]}},
    )
    labelFontStyle: FontStyleEnum = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Legend"]}},
    )
    labelFontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Legend"]}},
    )
    legendX: float = Field(
        default=...,
        description="""The pixel x-coordinate of the legend group.""",
        json_schema_extra={"linkml_meta": {"alias": "legendX", "domain_of": ["Legend"]}},
    )
    legendY: float = Field(
        default=...,
        description="""The pixel y-coordinate of the legend group.""",
        json_schema_extra={"linkml_meta": {"alias": "legendY", "domain_of": ["Legend"]}},
    )
    zindex: float = Field(
        default=...,
        description="""The integer z-index indicating the layering of the legend group relative to other axis, mark, and 
legend groups.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Legend"]}},
    )

    @field_validator("fill")
    def pattern_fill(cls, v):
        pattern = re.compile(r"^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fill format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fill format: {v}"
            raise ValueError(err_msg)
        return v


class CategoricalLegend(Legend):
    """
    Type of legend for categorical data.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/legends"})

    columns: Optional[int] = Field(
        default=None,
        description="""The number of columns in which to arrange symbol legend entries. A value of 0 or lower indicates a single row 
with one column per entry. The default is 0 for horizontal symbol legends and 1 for vertical symbol legends.""",
        json_schema_extra={"linkml_meta": {"alias": "columns", "domain_of": ["CategoricalLegend"]}},
    )
    columnPadding: Optional[float] = Field(
        default=None,
        description="""The horizontal padding in pixels between symbol legend entries.""",
        json_schema_extra={"linkml_meta": {"alias": "columnPadding", "domain_of": ["CategoricalLegend"]}},
    )
    rowPadding: Optional[float] = Field(
        default=None,
        description="""The vertical padding in pixels between symbol legend entries.""",
        json_schema_extra={"linkml_meta": {"alias": "rowPadding", "domain_of": ["CategoricalLegend"]}},
    )
    type: LegendType = Field(
        default=...,
        description="""The type of legend, either 'gradient' (continuous data) or 'discrete' (categorical data).""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Legend"]}},
    )
    direction: LegendDirections = Field(
        default=...,
        description="""The direction of the legend, one of 'vertical' or 'horizontal'.""",
        json_schema_extra={"linkml_meta": {"alias": "direction", "domain_of": ["Legend"]}},
    )
    orient: Optional[Literal["none"]] = Field(
        default="none",
        description="""The orientation of the legend, determining where the legend is placed relative to a chart's data rectangle. 
Currently, only 'none' is allowed here as in Vega this allows to directly specify the positioning in 
pixel coordinates. If there is demand, this can be changed.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "orient",
                "domain_of": ["Title", "Legend"],
                "equals_string": "none",
                "ifabsent": "string(none)",
            }
        },
    )
    padding: Optional[float] = Field(
        default=None,
        description="""The padding between the border and content of the legend group in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "padding", "domain_of": ["Legend"]}},
    )
    fill: str = Field(
        default=...,
        description="""The name of a scale that maps to a fill color. This represents the color used to visualize discrete classes
or continuous data in the legend.""",
        json_schema_extra={"linkml_meta": {"alias": "fill", "domain_of": ["Legend"]}},
    )
    fillColor: Optional[str] = Field(
        default=None,
        description="""Hex string representing a RGBA color, which is the background color of the legend.""",
        json_schema_extra={"linkml_meta": {"alias": "fillColor", "domain_of": ["Legend"], "slot_uri": "rgbaHexSlot"}},
    )
    strokeColor: Optional[str] = Field(
        default=None,
        description="""Hex string representing a RGBA color, which is the color of the legend border.""",
        json_schema_extra={"linkml_meta": {"alias": "strokeColor", "domain_of": ["Legend"], "slot_uri": "rgbaHexSlot"}},
    )
    strokeWidth: Optional[float] = Field(
        default=None,
        description="""The width of the legend border in pixels. This property deviates from its Vega equivalent, in that the 
vega equivalent expects a 'Scale'.""",
        json_schema_extra={"linkml_meta": {"alias": "strokeWidth", "domain_of": ["Legend"]}},
    )
    labelOffset: float = Field(
        default=...,
        description="""Offset in pixels between legend labels their corresponding symbol or gradient.""",
        json_schema_extra={"linkml_meta": {"alias": "labelOffset", "domain_of": ["Legend"]}},
    )
    labelAlign: HorizontalAlignEnum = Field(
        default=...,
        description="""Horizontal text alignment for legend labels. In short this means where the label text is relative to the
anchor point of the labels (this could be defined as the coordinates where the labels are specified to be).""",
        json_schema_extra={"linkml_meta": {"alias": "labelAlign", "domain_of": ["Legend"]}},
    )
    labelColor: str = Field(
        default=...,
        description="""Text color for legend labels represented by a RGB hex string.""",
        json_schema_extra={"linkml_meta": {"alias": "labelColor", "domain_of": ["Legend"], "slot_uri": "rgbHexSlot"}},
    )
    labelOpacity: str = Field(
        default=...,
        description="""The opacity of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Legend"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default="Arial",
        description="""Font name for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFont", "domain_of": ["Legend"], "ifabsent": "string(Arial)"}},
    )
    labelFontSize: float = Field(
        default=...,
        description="""Font size in pixels for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Legend"]}},
    )
    labelFontStyle: FontStyleEnum = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Legend"]}},
    )
    labelFontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Legend"]}},
    )
    legendX: float = Field(
        default=...,
        description="""The pixel x-coordinate of the legend group.""",
        json_schema_extra={"linkml_meta": {"alias": "legendX", "domain_of": ["Legend"]}},
    )
    legendY: float = Field(
        default=...,
        description="""The pixel y-coordinate of the legend group.""",
        json_schema_extra={"linkml_meta": {"alias": "legendY", "domain_of": ["Legend"]}},
    )
    zindex: float = Field(
        default=...,
        description="""The integer z-index indicating the layering of the legend group relative to other axis, mark, and 
legend groups.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Legend"]}},
    )

    @field_validator("fill")
    def pattern_fill(cls, v):
        pattern = re.compile(r"^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fill format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fill format: {v}"
            raise ValueError(err_msg)
        return v


class ColorBarLegend(Legend):
    """
    Type of legend for continuous data.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/legends"})

    gradientLength: float = Field(
        default=...,
        description="""The length in pixels of the primary axis of a color gradient. This value corresponds to the height of a 
vertical gradient or the width of a horizontal gradient.""",
        json_schema_extra={"linkml_meta": {"alias": "gradientLength", "domain_of": ["ColorBarLegend"]}},
    )
    gradientOpacity: str = Field(
        default=...,
        description="""Opacity of the color gradient.""",
        json_schema_extra={
            "linkml_meta": {"alias": "gradientOpacity", "domain_of": ["ColorBarLegend"], "slot_uri": "opacityValueSlot"}
        },
    )
    gradientStrokeColor: str = Field(
        default=...,
        description="""Stroke color of the color gradient border.""",
        json_schema_extra={
            "linkml_meta": {"alias": "gradientStrokeColor", "domain_of": ["ColorBarLegend"], "slot_uri": "rgbHexSlot"}
        },
    )
    gradientStrokeWidth: float = Field(
        default=...,
        description="""Stroke width of the color gradient border.""",
        json_schema_extra={"linkml_meta": {"alias": "gradientStrokeWidth", "domain_of": ["ColorBarLegend"]}},
    )
    type: LegendType = Field(
        default=...,
        description="""The type of legend, either 'gradient' (continuous data) or 'discrete' (categorical data).""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Legend"]}},
    )
    direction: LegendDirections = Field(
        default=...,
        description="""The direction of the legend, one of 'vertical' or 'horizontal'.""",
        json_schema_extra={"linkml_meta": {"alias": "direction", "domain_of": ["Legend"]}},
    )
    orient: Optional[Literal["none"]] = Field(
        default="none",
        description="""The orientation of the legend, determining where the legend is placed relative to a chart's data rectangle. 
Currently, only 'none' is allowed here as in Vega this allows to directly specify the positioning in 
pixel coordinates. If there is demand, this can be changed.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "orient",
                "domain_of": ["Title", "Legend"],
                "equals_string": "none",
                "ifabsent": "string(none)",
            }
        },
    )
    padding: Optional[float] = Field(
        default=None,
        description="""The padding between the border and content of the legend group in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "padding", "domain_of": ["Legend"]}},
    )
    fill: str = Field(
        default=...,
        description="""The name of a scale that maps to a fill color. This represents the color used to visualize discrete classes
or continuous data in the legend.""",
        json_schema_extra={"linkml_meta": {"alias": "fill", "domain_of": ["Legend"]}},
    )
    fillColor: Optional[str] = Field(
        default=None,
        description="""Hex string representing a RGBA color, which is the background color of the legend.""",
        json_schema_extra={"linkml_meta": {"alias": "fillColor", "domain_of": ["Legend"], "slot_uri": "rgbaHexSlot"}},
    )
    strokeColor: Optional[str] = Field(
        default=None,
        description="""Hex string representing a RGBA color, which is the color of the legend border.""",
        json_schema_extra={"linkml_meta": {"alias": "strokeColor", "domain_of": ["Legend"], "slot_uri": "rgbaHexSlot"}},
    )
    strokeWidth: Optional[float] = Field(
        default=None,
        description="""The width of the legend border in pixels. This property deviates from its Vega equivalent, in that the 
vega equivalent expects a 'Scale'.""",
        json_schema_extra={"linkml_meta": {"alias": "strokeWidth", "domain_of": ["Legend"]}},
    )
    labelOffset: float = Field(
        default=...,
        description="""Offset in pixels between legend labels their corresponding symbol or gradient.""",
        json_schema_extra={"linkml_meta": {"alias": "labelOffset", "domain_of": ["Legend"]}},
    )
    labelAlign: HorizontalAlignEnum = Field(
        default=...,
        description="""Horizontal text alignment for legend labels. In short this means where the label text is relative to the
anchor point of the labels (this could be defined as the coordinates where the labels are specified to be).""",
        json_schema_extra={"linkml_meta": {"alias": "labelAlign", "domain_of": ["Legend"]}},
    )
    labelColor: str = Field(
        default=...,
        description="""Text color for legend labels represented by a RGB hex string.""",
        json_schema_extra={"linkml_meta": {"alias": "labelColor", "domain_of": ["Legend"], "slot_uri": "rgbHexSlot"}},
    )
    labelOpacity: str = Field(
        default=...,
        description="""The opacity of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Legend"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default="Arial",
        description="""Font name for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFont", "domain_of": ["Legend"], "ifabsent": "string(Arial)"}},
    )
    labelFontSize: float = Field(
        default=...,
        description="""Font size in pixels for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Legend"]}},
    )
    labelFontStyle: FontStyleEnum = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Legend"]}},
    )
    labelFontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Legend"]}},
    )
    legendX: float = Field(
        default=...,
        description="""The pixel x-coordinate of the legend group.""",
        json_schema_extra={"linkml_meta": {"alias": "legendX", "domain_of": ["Legend"]}},
    )
    legendY: float = Field(
        default=...,
        description="""The pixel y-coordinate of the legend group.""",
        json_schema_extra={"linkml_meta": {"alias": "legendY", "domain_of": ["Legend"]}},
    )
    zindex: float = Field(
        default=...,
        description="""The integer z-index indicating the layering of the legend group relative to other axis, mark, and 
legend groups.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Legend"]}},
    )

    @field_validator("fill")
    def pattern_fill(cls, v):
        pattern = re.compile(r"^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid fill format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid fill format: {v}"
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
Legend.model_rebuild()
CategoricalLegend.model_rebuild()
ColorBarLegend.model_rebuild()

