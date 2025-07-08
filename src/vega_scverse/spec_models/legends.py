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


class LabelAlignValues(str, Enum):
    """
    The possible values for horizontal alignment of the legend labels.
    """

    left = "left"
    """
    The anchor point of the labels is left of the label text.
    """
    center = "center"
    """
    The anchor point of the labels is at the center of the label text.
    """
    right = "right"
    """
    The anchor point of the labels is right of the label text.
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
    fontSize: str = Field(
        default=...,
        description="""Font size in pixels of the title text.""",
        json_schema_extra={
            "linkml_meta": {"alias": "fontSize", "domain_of": ["Title"], "slot_uri": "nonNegativeFloatSlot"}
        },
    )
    fontStyle: FontStyleValues = Field(
        default=...,
        description="""Fontstyle of the title.""",
        json_schema_extra={"linkml_meta": {"alias": "fontStyle", "domain_of": ["Title"]}},
    )
    fontWeight: FontWeightValues = Field(
        default=...,
        description="""Font weight of the title""",
        json_schema_extra={"linkml_meta": {"alias": "fontWeight", "domain_of": ["Title"]}},
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


class CircleShape(ConfiguredBaseModel):
    """
    Circle shape definition used in symbol mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

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
        description="""The orientation of the legend, determining where the legend is placed relative to a chart’s data rectangle. 
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
    labelAlign: LabelAlignValues = Field(
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
    labelFontStyle: str = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Legend"], "slot_uri": "FontStyleValues"}
        },
    )
    labelFontWeight: str = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Legend"], "slot_uri": "FontWeightValues"}
        },
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
        description="""The orientation of the legend, determining where the legend is placed relative to a chart’s data rectangle. 
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
    labelAlign: LabelAlignValues = Field(
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
    labelFontStyle: str = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Legend"], "slot_uri": "FontStyleValues"}
        },
    )
    labelFontWeight: str = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Legend"], "slot_uri": "FontWeightValues"}
        },
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
        description="""The orientation of the legend, determining where the legend is placed relative to a chart’s data rectangle. 
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
    labelAlign: LabelAlignValues = Field(
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
    labelFontStyle: str = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Legend"], "slot_uri": "FontStyleValues"}
        },
    )
    labelFontWeight: str = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Legend"], "slot_uri": "FontWeightValues"}
        },
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
RGBHexItem.model_rebuild()
RandomRGBSignal.model_rebuild()
Title.model_rebuild()
Padding.model_rebuild()
ColorItem.model_rebuild()
CircleShape.model_rebuild()
AxisItem.model_rebuild()
Legend.model_rebuild()
CategoricalLegend.model_rebuild()
ColorBarLegend.model_rebuild()

