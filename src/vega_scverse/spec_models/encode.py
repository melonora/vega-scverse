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
        "description": "Vega like specification for the encodings used to specify the "
        "visuals representation of marks.",
        "id": "https://w3id.org/scverse/vega-scverse/encode",
        "imports": ["linkml:types", "misc", "slots"],
        "license": "BSD-3",
        "name": "vega-scverse-encode",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": "src\\vega_scverse\\schema\\encode.yaml",
        "title": "vega-scverse-encode",
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
                    "CircleShape",
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
                    "CircleShape",
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
                    "CircleShape",
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
                    "CircleShape",
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
                    "CircleShape",
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
                    "CircleShape",
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
                    "CircleShape",
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
                    "CircleShape",
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
        json_schema_extra={"linkml_meta": {"alias": "text", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    orient: OrientEnum = Field(
        default=...,
        description="""The orientation of the title relative to the chart.""",
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Title"]}},
    )
    baseline: BaseLineEnum = Field(
        default=...,
        description="""The baseline attribute specifies the vertical alignment (baseline) of the text relative to its y-coordinate.""",
        json_schema_extra={"linkml_meta": {"alias": "baseline", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    color: str = Field(
        default=...,
        description="""Text color of the title text.""",
        json_schema_extra={"linkml_meta": {"alias": "color", "domain_of": ["Title"], "slot_uri": "rgbaHexSlot"}},
    )
    font: str = Field(
        default=...,
        description="""Font name of the title text.""",
        json_schema_extra={"linkml_meta": {"alias": "font", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    fontSize: str = Field(
        default=...,
        description="""Font size in pixels of the title text.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fontSize",
                "domain_of": ["Title", "TextEncodeEnter"],
                "slot_uri": "nonNegativeFloatSlot",
            }
        },
    )
    fontStyle: FontStyleEnum = Field(
        default=...,
        description="""Fontstyle of the title.""",
        json_schema_extra={"linkml_meta": {"alias": "fontStyle", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    fontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of the title""",
        json_schema_extra={"linkml_meta": {"alias": "fontWeight", "domain_of": ["Title", "TextEncodeEnter"]}},
    )


class Padding(ConfiguredBaseModel):
    """
    padding defines the amount of space (in pixels) to reserve between the edge of the chart container and the inner
    view area where data marks are rendered. It acts as an internal margin that ensures visual elements like axes,
    titles, and legends don’t touch or overflow the chart’s outer boundaries.
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
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: str = Field(
        default=...,
        description="""The value or field to which to apply the color.""",
        json_schema_extra={
            "linkml_meta": {"alias": "field", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
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
                    "CircleShape",
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
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: AxisEnum = Field(
        default=...,
        description="""The mark's field value transformed by the scale. Either x or y.""",
        json_schema_extra={
            "linkml_meta": {"alias": "field", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
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
            "linkml_meta": {
                "alias": "enter",
                "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode", "TextEncode", "GroupEncode"],
            }
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
            "linkml_meta": {
                "alias": "enter",
                "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode", "TextEncode", "GroupEncode"],
            }
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
            "linkml_meta": {
                "alias": "enter",
                "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode", "TextEncode", "GroupEncode"],
            }
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
            "linkml_meta": {
                "alias": "enter",
                "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode", "TextEncode", "GroupEncode"],
            }
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


class TextEncode(ConfiguredBaseModel):
    """
    A set of visual encoding properties that determine the position and appearance of a text mark.
    In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data
    is processed for the first time and a mark instance is newly added to a scene and are the only properties
    supported for a text mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    enter: TextEncodeEnter = Field(
        default=...,
        description="""Enter properties that are evaluated when data for a text mark is processed for the first time and the 
group mark is newly added to a scene.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "enter",
                "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode", "TextEncode", "GroupEncode"],
            }
        },
    )


class GroupEncode(ConfiguredBaseModel):
    """
    A set of visual encoding properties that determine the position of a group mark, which are used for subplots.
    In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data
    is processed for the first time and a mark instance is newly added to a scene and are the only properties
    supported for a group mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    enter: GroupEncodeEnter = Field(
        default=...,
        description="""Enter properties that are evaluated when data for a group mark is processed for the first time and the 
group mark is newly added to a scene.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "enter",
                "domain_of": ["ImageEncode", "LabelEncode", "SymbolEncode", "PathEncode", "TextEncode", "GroupEncode"],
            }
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
        description="""The opacity of the image mark.""",
        json_schema_extra={
            "linkml_meta": {"alias": "opacity", "domain_of": ["ImageEncodeEnter"], "slot_uri": "opacityValueSlot"}
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
                    "TextEncodeEnter",
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
                    "TextEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )
    fillOpacity: str = Field(
        default=...,
        description="""Opacity value for the label fill between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
                "slot_uri": "opacityValueSlot",
            }
        },
    )
    strokeOpacity: str = Field(
        default=...,
        description="""Opacity value for the label stroke between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
                "slot_uri": "opacityValueSlot",
            }
        },
    )
    strokeWidth: str = Field(
        default=...,
        description="""The width of the label outlines in pixels.""",
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "x",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    y: AxisItem = Field(
        default=...,
        description="""The y coordinates""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "y",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    stroke: Union[ColorItem, RGBHexItem] = Field(
        default=...,
        description="""The color of the outline of each individual point.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "stroke",
                "any_of": [{"range": "ColorItem"}, {"range": "RGBHexItem"}],
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
            }
        },
    )
    fill: Union[ColorItem, RGBHexItem] = Field(
        default=...,
        description="""The color fill of each individual point.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ColorItem"}, {"range": "RGBHexItem"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "TextEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )
    fillOpacity: str = Field(
        default=...,
        description="""Opacity value for the point fill between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
                "slot_uri": "opacityValueSlot",
            }
        },
    )
    strokeOpacity: str = Field(
        default=...,
        description="""Opacity value for the point outlines between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter"],
                "slot_uri": "opacityValueSlot",
            }
        },
    )
    strokeWidth: str = Field(
        default=...,
        description="""The width of the point outlines in pixels.""",
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
        description="""The points bounding box area size (typographic points are 1/72 in.).""",
        json_schema_extra={"linkml_meta": {"alias": "size", "domain_of": ["PointsEncodeEnter"], "slot_uri": "size"}},
    )
    shape: CircleShape = Field(
        default=...,
        description="""The type of shape. In this case `circle`.""",
        json_schema_extra={"linkml_meta": {"alias": "shape", "domain_of": ["PointsEncodeEnter"]}},
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "x",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    y: AxisItem = Field(
        default=...,
        description="""The y coordinates""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "y",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    fill: Union[ColorItem, RGBHexItem] = Field(
        default=...,
        description="""The color fill of each individual label.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ColorItem"}, {"range": "RGBHexItem"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "TextEncodeEnter",
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
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
                "slot_uri": "opacityValueSlot",
            }
        },
    )


class TextEncodeEnter(ConfiguredBaseModel):
    """
    Enter properties that are evaluated when data for a text mark is processed for the first time and the
    group mark is newly added to a scene.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    x: PositionItem = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "x",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    y: PositionItem = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "y",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    text: TextItem = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "text", "domain_of": ["Title", "TextEncodeEnter"]}}
    )
    align: HorizontalAlignEnum = Field(
        default=...,
        description="""The horizontal text alignment relative to the text anchor point.""",
        json_schema_extra={"linkml_meta": {"alias": "align", "domain_of": ["TextEncodeEnter"]}},
    )
    angle: Optional[float] = Field(
        default=None,
        description="""The rotation angle of the text in degrees.""",
        ge=0,
        le=359,
        json_schema_extra={"linkml_meta": {"alias": "angle", "domain_of": ["TextEncodeEnter"]}},
    )
    baseline: BaseLineEnum = Field(
        default=...,
        description="""The baseline attribute specifies the vertical alignment (baseline) of the text relative to its y-coordinate.""",
        json_schema_extra={"linkml_meta": {"alias": "baseline", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    font: FontItem = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "font", "domain_of": ["Title", "TextEncodeEnter"]}}
    )
    fontSize: FontSizeItem = Field(
        default=..., json_schema_extra={"linkml_meta": {"alias": "fontSize", "domain_of": ["Title", "TextEncodeEnter"]}}
    )
    fontWeight: FontWeightItem = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "fontWeight", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    fontStyle: FontStyleItem = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"alias": "fontStyle", "domain_of": ["Title", "TextEncodeEnter"]}},
    )
    fill: RGBHexItem = Field(
        default=...,
        description="""The color of the text""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "TextEncodeEnter",
                    "MarkEncodeUpdate",
                ],
            }
        },
    )
    fillOpacity: Optional[str] = Field(
        default=None,
        description="""Opacity of the text.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
                "slot_uri": "opacityValueSlot",
            }
        },
    )


class GroupEncodeEnter(ConfiguredBaseModel):
    """
    Encoding for the position, width and height of a group mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    x: float = Field(
        default=...,
        description="""Placing of the group mark along the x axis (width of the complete charter). The origin
is on the left side.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "x",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    y: float = Field(
        default=...,
        description="""Placing of the group mark along the y axis (height of the complete charter). The origin
is on the top side.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "y",
                "domain_of": ["PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter", "GroupEncodeEnter"],
            }
        },
    )
    width: float = Field(
        default=...,
        description="""The width of the mark in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "width", "domain_of": ["GroupEncodeEnter"]}},
    )
    height: float = Field(
        default=...,
        description="""The height of the mark in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "height", "domain_of": ["GroupEncodeEnter"]}},
    )


class MarkEncodeUpdate(ConfiguredBaseModel):
    """
    Update properties that are evaluated for all existing (non-exiting) mark instances.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    fill: Optional[list[Union[ConditionalFillUpdate, RGBHexItem]]] = Field(
        default=None,
        description="""Update of fill color based on a test condition and optional a backup static fill value""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [{"range": "ConditionalFillUpdate"}, {"range": "RGBHexItem"}],
                "domain_of": [
                    "ImageEncodeEnter",
                    "LabelEncodeEnter",
                    "PointsEncodeEnter",
                    "PathEncodeEnter",
                    "TextEncodeEnter",
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
            "linkml_meta": {"alias": "field", "domain_of": ["ColorItem", "AxisItem", "ConditionalFillUpdate"]}
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
CircleShape.model_rebuild()
AxisItem.model_rebuild()
ImageEncode.model_rebuild()
LabelEncode.model_rebuild()
SymbolEncode.model_rebuild()
PathEncode.model_rebuild()
TextEncode.model_rebuild()
GroupEncode.model_rebuild()
ImageEncodeEnter.model_rebuild()
LabelEncodeEnter.model_rebuild()
PointsEncodeEnter.model_rebuild()
PathEncodeEnter.model_rebuild()
TextEncodeEnter.model_rebuild()
GroupEncodeEnter.model_rebuild()
MarkEncodeUpdate.model_rebuild()
ConditionalFillUpdate.model_rebuild()

