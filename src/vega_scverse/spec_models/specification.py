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
        "imports": ["linkml:types", "linkml_data", "linkml_scales", "axes", "legends", "marks", "misc"],
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
        "source_file": "src\\vega_scverse\\schema\\specification.yaml",
        "title": "vega-scverse-specification",
    }
)


class TransformTypeEnum(str, Enum):
    """
    Valid transforms on a data stream within a scverse viewconfig.
    """

    filter_element = "filter_element"
    """
    Filter an element from a root data object, like a SpatialData zarr.
    """
    filter_cs = "filter_cs"
    """
    Filter the coordinate systems of an element to point to coordinate system the element is displayed in.
    """
    filter_scale = "filter_scale"
    """
    Filter on a particular scale in multiscale raster data.
    """
    filter_channel = "filter_channel"
    """
    Filter on a particular channel in raster data.
    """
    aggregate = "aggregate"
    """
    Group and summarize an input data stream to produce a derived output stream.
    """
    spread = "spread"
    """
    Expand each pixel in a rasterized image by a specified number of pixels to make sparse data more visible.
    """
    lookup = "lookup"
    """
    Extend a primary data stream by looking up values on a secondary data stream.
    """
    formula = "formula"
    """
    Apply a formula to a data input stream.
    """


class AggregateOpsEnum(str, Enum):
    """
        The summary statistic to apply for an aggregation transform. The summary statistic is calculated per datashade
    raster pixel.
    """

    any = "any"
    max = "max"
    """
    Maximum value of all elements in each datashade raster pixel.
    """
    min = "min"
    """
    Minimum value of all elements in each datashade raster pixel.
    """
    mean = "mean"
    """
    Mean value of all elements in each datashade raster pixel.
    """
    stdev = "stdev"
    """
    Standard deviation of all elements in each datashade raster pixel.
    """
    sum = "sum"
    """
    Sum of all elements in each datashade raster pixel
    """
    variance = "variance"
    """
    Variance of all elements in each datashade raster pixel.
    """
    count = "count"
    """
    Count elements each datashade raster pixel, returning the result as a uint32, or a float32 if using 
    antialiasing.
    """


class ScaleEnum(str, Enum):
    """
    Possible values for the type of Scale
    """

    linear = "linear"
    """
    Maps continuous numeric data to a continuous range.
    """
    ordinal = "ordinal"
    """
    Maps discrete values (categories) to distinct values in the output range.
    """


class AxisRangeEnum(str, Enum):
    """
    Possible values which to map the data domain to.
    """

    height = "height"
    """
    Referring to the height of the plotting area.
    """
    width = "width"
    """
    Referring to the width of the plotting area.
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


class DataObject(ConfiguredBaseModel):
    """
    Abstract class for Vega like data set definitions and transforms that define the data based on scverse data
    models like SpatialData and AnnData to load and how to process it.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/data"}
    )

    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )
    format: str = Field(
        default=...,
        description="""Format object containing the type of data as object and a string or float value representing the version.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": ["DataObject", "SpatialDataObject", "BaseTableObject", "SpatialDataElementObject"],
            }
        },
    )

    @field_validator("name")
    def pattern_name(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class SpatialDataObject(DataObject):
    """
    SpatialData object specific to the SpatialData root
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    url: str = Field(
        default=...,
        description="""The absolute path to the SpatialData zarr.""",
        json_schema_extra={"linkml_meta": {"alias": "url", "domain_of": ["SpatialDataObject"]}},
    )
    format: Optional[SpatialDataFormat] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": ["DataObject", "SpatialDataObject", "BaseTableObject", "SpatialDataElementObject"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )

    @field_validator("name")
    def pattern_name(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class BaseTableObject(DataObject):
    """
    AnnData Table object stream.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    format: ElementFormat = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": ["DataObject", "SpatialDataObject", "BaseTableObject", "SpatialDataElementObject"],
            }
        },
    )
    source: str = Field(
        default=...,
        description="""The source of the SpatialData element. Must be the name / identifier of a SpatialData Object in the 
view configuration.""",
        json_schema_extra={
            "linkml_meta": {"alias": "source", "domain_of": ["BaseTableObject", "SpatialDataElementObject"]}
        },
    )
    transform: list[FilterTransform] = Field(
        default=...,
        description="""An array containing a single transform 'filter_element' with an expression stating which table to obtain
from the source SpatialData object stream.""",
        json_schema_extra={
            "linkml_meta": {"alias": "transform", "domain_of": ["BaseTableObject", "SpatialDataElementObject"]}
        },
    )
    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )

    @field_validator("source")
    def pattern_source(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid source format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid source format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("name")
    def pattern_name(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class SpatialDataElementObject(DataObject):
    """
    Data object pertaining to an element within the SpatialData object.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    format: ElementFormat = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": ["DataObject", "SpatialDataObject", "BaseTableObject", "SpatialDataElementObject"],
            }
        },
    )
    source: str = Field(
        default=...,
        description="""The source of the SpatialData element. Must be the name / identifier of a SpatialData Object in the 
view configuration.""",
        json_schema_extra={
            "linkml_meta": {"alias": "source", "domain_of": ["BaseTableObject", "SpatialDataElementObject"]}
        },
    )
    transform: list[
        Union[
            AggregateTransform,
            FilterChannelTransform,
            FilterTransform,
            LookupTransform,
            NormalizationFormulaTransform,
            SpreadTransform,
        ]
    ] = Field(
        default=...,
        description="""An array of transforms applied to the SpatialData element. The first transform is always `filter_element`,
which filters the SpatialData source object based on the element name. This is followed by `filter_cs`, to
specify in which coordinate system the element should be visualized. This can be followed by other optional
transforms.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "transform",
                "any_of": [
                    {"range": "LookupTransform"},
                    {"range": "FilterTransform"},
                    {"range": "FilterChannelTransform"},
                    {"range": "AggregateTransform"},
                    {"range": "SpreadTransform"},
                    {"range": "NormalizationFormulaTransform"},
                ],
                "domain_of": ["BaseTableObject", "SpatialDataElementObject"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )

    @field_validator("source")
    def pattern_source(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid source format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid source format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("name")
    def pattern_name(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class Transform(ConfiguredBaseModel):
    """
    Transform of data applied to data input.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/data"}
    )

    type: TransformTypeEnum = Field(
        default=...,
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
    )


class FilterTransform(Transform):
    """
    Select objects from a data stream to keep based on a filter expression. If the value of the filter expression
    is a single element, e.g. 'blobs_image', then the expression is equivalent to 'datum.value == blobs_image'.
    These are the first transforms in the array of transforms usually when visualizing SpatialData elements.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/data",
            "slot_usage": {
                "type": {
                    "description": "The type of filter transform. "
                    "'filter_element' will filter / select "
                    "a particular element from a data "
                    "source,\n"
                    "'filter_cs' will select the "
                    "coordinate system in which the "
                    "element should be visualized and "
                    "'filter_scale'\n"
                    "will select the scale of a multiscale "
                    "raster data element.",
                    "equals_string_in": ["filter_element", "filter_cs", "filter_scale"],
                    "name": "type",
                }
            },
        }
    )

    expr: str = Field(
        default=...,
        description="""Either the name of the element or coordinate system to filter / select.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "expr",
                "domain_of": ["FilterTransform", "FilterChannelTransform", "NormalizationFormulaTransform"],
            }
        },
    )
    type: Literal["filter_element", "filter_cs", "filter_scale"] = Field(
        default=...,
        description="""The type of filter transform. 'filter_element' will filter / select a particular element from a data source,
'filter_cs' will select the coordinate system in which the element should be visualized and 'filter_scale'
will select the scale of a multiscale raster data element.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string_in": ["filter_element", "filter_cs", "filter_scale"],
            }
        },
    )


class FilterChannelTransform(Transform):
    """
    Filter on particular channels in a raster data object.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/data",
            "slot_usage": {
                "type": {
                    "description": "The type of filter transform. "
                    "'filter_element' will filter / select "
                    "a particular element from a data "
                    "source,\n"
                    "'filter_cs' will select the "
                    "coordinate system in which the "
                    "element should be visualized and "
                    "'filter_scale'\n"
                    "will select the scale of a multiscale "
                    "raster data element.",
                    "equals_string": "filter_channel",
                    "name": "type",
                }
            },
        }
    )

    expr: Optional[list[Union[int, str]]] = Field(
        default=None,
        description="""The channel(s) to filter the input data stream on. Either a list of integers that correspond to the channel
indices or list of strings that refer to the name of the channels. Preferably, it SHOULD be the latter to
prevent a different context when ordering of the channels changes.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "expr",
                "any_of": [{"range": "string"}, {"range": "integer"}],
                "domain_of": ["FilterTransform", "FilterChannelTransform", "NormalizationFormulaTransform"],
            }
        },
    )
    type: Literal["filter_channel"] = Field(
        default=...,
        description="""The type of filter transform. 'filter_element' will filter / select a particular element from a data source,
'filter_cs' will select the coordinate system in which the element should be visualized and 'filter_scale'
will select the scale of a multiscale raster data element.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "filter_channel",
            }
        },
    )


class LookupTransform(Transform):
    """
    Transform extending a primary data stream by looking up values on a secondary data stream.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/data",
            "slot_usage": {"type": {"equals_string": "lookup", "ifabsent": "string(lookup)", "name": "type"}},
        }
    )

    from_: str = Field(
        default=...,
        description="""The name of the secondary data stream upon which to perform the lookup.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["LookupTransform", "Mark"]}},
    )
    key: str = Field(
        default=...,
        description="""The key field on the secondary stream, e.g. in table lookup it would be for example instance_id.""",
        json_schema_extra={"linkml_meta": {"alias": "key", "domain_of": ["LookupTransform"]}},
    )
    fields: list[str] = Field(
        default=...,
        description="""The data fields to copy from the secondary stream to the primary stream.""",
        json_schema_extra={"linkml_meta": {"alias": "fields", "domain_of": ["LookupTransform"]}},
    )
    values: list[str] = Field(
        default=...,
        description="""To be added""",
        json_schema_extra={"linkml_meta": {"alias": "values", "domain_of": ["LookupTransform", "Axis"]}},
    )
    as_: list[str] = Field(
        default=...,
        description="""To be added""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "LookupTransform",
                    "AggregateTransform",
                    "SpreadTransform",
                    "NormalizationFormulaTransform",
                ],
            }
        },
    )
    default: Optional[str] = Field(
        default=None,
        description="""The default value to assign if lookup fails""",
        json_schema_extra={"linkml_meta": {"alias": "default", "domain_of": ["LookupTransform"]}},
    )
    type: Literal["lookup"] = Field(
        default="lookup",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "lookup",
                "ifabsent": "string(lookup)",
            }
        },
    )

    @field_validator("from_")
    def pattern_from_(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid from_ format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid from_ format: {v}"
            raise ValueError(err_msg)
        return v


class AggregateTransform(Transform):
    """
    Group and summarize an input data stream to produce a derived output stream using particular summary statistics
    operations, e.g. sum, average etc..
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/data",
            "slot_usage": {"type": {"equals_string": "aggregate", "ifabsent": "string(aggregate)", "name": "type"}},
        }
    )

    field: list[str] = Field(
        default=...,
        description="""The data fields for which to compute aggregate functions. This array should align with the as 
arrays.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": [
                    "AggregateTransform",
                    "SpreadTransform",
                    "ContinuousColorDomain",
                    "ColorItem",
                    "AxisItem",
                    "ConditionalFillUpdate",
                ],
            }
        },
    )
    ops: list[AggregateOpsEnum] = Field(
        default=...,
        description="""The summary statistic to apply per field. This deviates from vega where ops has a single string value
while here it is an array with a length equal to 'field' and 'as'.""",
        json_schema_extra={"linkml_meta": {"alias": "ops", "domain_of": ["AggregateTransform"]}},
    )
    as_: list[str] = Field(
        default=...,
        description="""The output field names to use for each aggregated field in fields. In the initial implementation this is
the same as the values in 'field'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "LookupTransform",
                    "AggregateTransform",
                    "SpreadTransform",
                    "NormalizationFormulaTransform",
                ],
            }
        },
    )
    type: Literal["aggregate"] = Field(
        default="aggregate",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "aggregate",
                "ifabsent": "string(aggregate)",
            }
        },
    )


class SpreadTransform(Transform):
    """
    Datashade transform expanding each pixel in a rasterized image by a specified number of pixels to make sparse
    data more visible. This transform MUST be preceded by an aggregate transform and is optionally preceded by
    a normalization transform ('formula').
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/data",
            "slot_usage": {"type": {"equals_string": "spread", "ifabsent": "string(spread)", "name": "type"}},
        }
    )

    field: list[str] = Field(
        default=...,
        description="""The data fields on which to apply the spread transform. This array should align with the as 
arrays.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": [
                    "AggregateTransform",
                    "SpreadTransform",
                    "ContinuousColorDomain",
                    "ColorItem",
                    "AxisItem",
                    "ConditionalFillUpdate",
                ],
            }
        },
    )
    px: int = Field(
        default=...,
        description="""The amount of pixels by which to expand each pixel to make data more visible.""",
        json_schema_extra={"linkml_meta": {"alias": "px", "domain_of": ["SpreadTransform"]}},
    )
    as_: list[str] = Field(
        default=...,
        description="""The output field names to use for each field to which a spread transform is applied. In the initial 
implementation this is the same as the values in 'field'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "LookupTransform",
                    "AggregateTransform",
                    "SpreadTransform",
                    "NormalizationFormulaTransform",
                ],
            }
        },
    )
    type: Literal["spread"] = Field(
        default="spread",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "spread",
                "ifabsent": "string(spread)",
            }
        },
    )


class NormalizationFormulaTransform(Transform):
    """
    A formula to transform data.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/data",
            "slot_usage": {"type": {"equals_string": "formula", "ifabsent": "string(formula)", "name": "type"}},
        }
    )

    expr: str = Field(
        default=...,
        description="""Formula represented as string that in this case applies a normalization on the data. The column or field of 
data that is normalized is indicated as 'datum.<name_of_column>'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "expr",
                "domain_of": ["FilterTransform", "FilterChannelTransform", "NormalizationFormulaTransform"],
            }
        },
    )
    as_: str = Field(
        default=...,
        description="""The output field names to use for each field to which a normalization is applied.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "LookupTransform",
                    "AggregateTransform",
                    "SpreadTransform",
                    "NormalizationFormulaTransform",
                ],
            }
        },
    )
    type: Literal["formula"] = Field(
        default="formula",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "formula",
                "ifabsent": "string(formula)",
            }
        },
    )

    @field_validator("expr")
    def pattern_expr(cls, v):
        pattern = re.compile(
            r"(?:clamp\(\s*)?\(\s*datum\.\w+\s*[-+*/]\s*[\d.]+\s*\)\s*[-+*/]\s*\(\s*[\d.]+\s*[-+*/]\s*[\d.]+\s*\)(?:\s*,\s*[\d.]+\s*,\s*[\d.]+\s*\))?"
        )
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid expr format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid expr format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator("as_")
    def pattern_as_(cls, v):
        pattern = re.compile(r"^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid as_ format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid as_ format: {v}"
            raise ValueError(err_msg)
        return v


class BaseFormat(ConfiguredBaseModel):
    """
    Format object containing the type of data as object and a string value representing the version.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/data"}
    )

    type: str = Field(
        default=...,
        description="""The type of the data as string, e.g. RasterFormat""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
    )
    version: str = Field(
        default=...,
        description="""The version of the data type that is defined. Defined as semantic version + optional development release.
It is represented either as string value or float value.""",
        json_schema_extra={
            "linkml_meta": {"alias": "version", "domain_of": ["BaseFormat", "SpatialDataFormat", "ElementFormat"]}
        },
    )


class SpatialDataFormat(BaseFormat):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    version: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "version", "domain_of": ["BaseFormat", "SpatialDataFormat", "ElementFormat"]}
        },
    )
    type: str = Field(
        default=...,
        description="""The type of the data as string, e.g. RasterFormat""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
    )

    @field_validator("version")
    def pattern_version(cls, v):
        pattern = re.compile(r"^(\d+\.\d+)(\.\d+)?([a-zA-Z0-9.+-]*)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid version format: {v}"
            raise ValueError(err_msg)
        return v


class ElementFormat(BaseFormat):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    version: Optional[float] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {"alias": "version", "domain_of": ["BaseFormat", "SpatialDataFormat", "ElementFormat"]}
        },
    )
    type: str = Field(
        default=...,
        description="""The type of the data as string, e.g. RasterFormat""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
    )


class BaseScales(ConfiguredBaseModel):
    """
    Vega like definition for scales which specifies a collection of mappings from a data domain
    (e.g., numbers, categories, dates) to a visual range (e.g., position on the screen, color spectrum, size).
    Due to LinkML currently not supporting assigning classes as values for ranged in any_of, this class
    should be used as an abstract base class.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/scales"}
    )

    scales: Optional[list[str]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "scales",
                "any_of": [
                    {"range": "BaseAxisScale"},
                    {"range": "BaseCategoricalColorScale"},
                    {"range": "LinearColorScale"},
                ],
                "domain_of": ["BaseScales", "GroupMark", "ViewConfiguration"],
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
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and 
visual range, e.g. `linear`.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
    )


class BaseAxisScale(Scale):
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
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale", "Axis"],
            }
        },
    )
    range: AxisRangeEnum = Field(
        default=...,
        description="""Defines the target visual dimension for the axis scale's output range. Must be either 'width' for an X-axis 
scale or 'height' for a Y-axis scale. These keywords refer to the pixel extent of the plotting area, not the 
full canvas. The plotting area is the region where data marks are rendered, and its dimensions are typically 
defined by the top-level 'width' and 'height' properties of a Vega specification. For example, setting 
\"range\": \"height\" in a Y-axis scale maps the scale's domain to pixel positions from top to bottom within the 
plot area. This is commonly used to align data values with positional axes in coordinate-based visualizations.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "range",
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""`Y_scale` or `X_scale` optionally followed by `_n` where n stands for the index of the subplot.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )
    type: Literal["linear"] = Field(
        default="linear",
        description="""Only linear is supported for an `AxisScale` for now.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
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
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )
    type: ScaleEnum = Field(
        default=...,
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and 
visual range, e.g. `linear`.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
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


class LinearColorScale(ColorScale):
    """
    A vega like scale specifically for mapping from a linear continuous data domain to a visual color range.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/scverse/vega-scverse/scales",
            "slot_usage": {
                "type": {
                    "description": "Only linear is supported for an " "`LinearColorScale` for now.",
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
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale", "Axis"],
            }
        },
    )
    range: ContinuousColorMapRange = Field(
        default=...,
        description="""The range to which to map the data domain. In this case one that refers to a colormap range.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "range",
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""color followed by '_pseudoUUID' used to refer to this scale elsewhere in the view configuration.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )
    type: Literal["linear"] = Field(
        default="linear",
        description="""Only linear is supported for an `LinearColorScale` for now.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
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


class BaseCategoricalColorScale(ColorScale):
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
        description="""The data domain as a list of discrete string values. Length must be equal to the length of range""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "domain",
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale", "Axis"],
            }
        },
    )
    range: list[str] = Field(
        default=...,
        description="""List of RGB colors as hexadecimal strings. Length must be equal to length of domain""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "range",
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""color followed by '_pseudoUUID' used to refer to this scale elsewhere in the view configuration.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject", "Scale"]}},
    )
    type: Literal["ordinal"] = Field(
        default="ordinal",
        description="""The type of scale which is a description of what kind of mapping is performed between data domain and 
visual range, e.g. `linear`.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
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
    A data domain or source for a LinearColorScale.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/scales"})

    data: str = Field(
        default=...,
        description="""The identifier of the particular data object in the data array to which the color mapping in 
LinearColorScale must be applied. In Vega this is only defined when the type of Scale is
ordinal, but we deviate from that.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": ["ContinuousColorDomain", "MarkDataSource", "ViewConfiguration"],
            }
        },
    )
    field: str = Field(
        default=...,
        description="""If the data source is a table, then the field is the column within the table that is used as 
a source for the color mapping. In case of raster data with a single channel, the field equals
'value' and if multichannel raster data it is the name or index of the image channel.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": [
                    "AggregateTransform",
                    "SpreadTransform",
                    "ContinuousColorDomain",
                    "ColorItem",
                    "AxisItem",
                    "ConditionalFillUpdate",
                ],
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


class Axis(ConfiguredBaseModel):
    """
    An axis visualizes a spatial scale mapping for cartesian coordinates using ticks, grid lines and labels.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/axes"})

    scale: str = Field(
        default=...,
        description="""Name of the 'AxisScale' to visualize as axis object.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["Axis", "ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    orient: OrientEnum = Field(
        default=...,
        description="""The orientation of the axis, either 'left', 'right', 'top' or 'bottom'.""",
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Axis", "Legend", "Title"]}},
    )
    domain: bool = Field(
        default=...,
        description="""A boolean flag indicating if the domain (the axis baseline, the line that the ticks connect to) should be 
included as part of the axis.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "domain",
                "domain_of": ["BaseAxisScale", "LinearColorScale", "BaseCategoricalColorScale", "Axis"],
            }
        },
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
        json_schema_extra={
            "linkml_meta": {"alias": "labelColor", "domain_of": ["Axis", "Legend"], "slot_uri": "rgbHexSlot"}
        },
    )
    labelOpacity: Optional[float] = Field(
        default=None,
        description="""Opacity of axis tick labels.""",
        ge=0,
        le=1,
        json_schema_extra={"linkml_meta": {"alias": "labelOpacity", "domain_of": ["Axis", "Legend"]}},
    )
    labelFont: Optional[str] = Field(
        default=None,
        description="""Font name for axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFont", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontSize: Optional[float] = Field(
        default=None,
        description="""Font size of axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontStyle: Optional[FontStyleEnum] = Field(
        default=None,
        description="""Font style of axis tick labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontWeight: Optional[FontWeightEnum] = Field(
        default=None,
        description="""Font weight of axis tick labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Axis", "Legend"]}},
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
                "domain_of": ["LookupTransform", "Axis"],
            }
        },
    )
    zindex: float = Field(
        default=...,
        description="""The integer z-index indicating the layering of the axis group relative to other axis, mark, and legend groups. 
The default value is 0 and axes and grid lines are drawn behind any marks defined in the same specification 
level. Higher values (1) will cause axes and grid lines to be drawn on top of marks.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
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
                "domain_of": ["Axis", "Legend", "Title"],
                "equals_string": "none",
                "ifabsent": "string(none)",
            }
        },
    )
    padding: Optional[float] = Field(
        default=None,
        description="""The padding between the border and content of the legend group in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "padding", "domain_of": ["Legend", "ViewConfiguration"]}},
    )
    fill: str = Field(
        default=...,
        description="""The name of a scale that maps to a fill color. This represents the color used to visualize discrete classes
or continuous data in the legend.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "domain_of": [
                    "Legend",
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["Legend", "LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
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
        json_schema_extra={
            "linkml_meta": {"alias": "labelColor", "domain_of": ["Axis", "Legend"], "slot_uri": "rgbHexSlot"}
        },
    )
    labelOpacity: str = Field(
        default=...,
        description="""The opacity of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Axis", "Legend"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default="Arial",
        description="""Font name for legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFont", "domain_of": ["Axis", "Legend"], "ifabsent": "string(Arial)"}
        },
    )
    labelFontSize: float = Field(
        default=...,
        description="""Font size in pixels for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontStyle: FontStyleEnum = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Axis", "Legend"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
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
                "domain_of": ["Axis", "Legend", "Title"],
                "equals_string": "none",
                "ifabsent": "string(none)",
            }
        },
    )
    padding: Optional[float] = Field(
        default=None,
        description="""The padding between the border and content of the legend group in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "padding", "domain_of": ["Legend", "ViewConfiguration"]}},
    )
    fill: str = Field(
        default=...,
        description="""The name of a scale that maps to a fill color. This represents the color used to visualize discrete classes
or continuous data in the legend.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "domain_of": [
                    "Legend",
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["Legend", "LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
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
        json_schema_extra={
            "linkml_meta": {"alias": "labelColor", "domain_of": ["Axis", "Legend"], "slot_uri": "rgbHexSlot"}
        },
    )
    labelOpacity: str = Field(
        default=...,
        description="""The opacity of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Axis", "Legend"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default="Arial",
        description="""Font name for legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFont", "domain_of": ["Axis", "Legend"], "ifabsent": "string(Arial)"}
        },
    )
    labelFontSize: float = Field(
        default=...,
        description="""Font size in pixels for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontStyle: FontStyleEnum = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Axis", "Legend"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
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
                "domain_of": ["Axis", "Legend", "Title"],
                "equals_string": "none",
                "ifabsent": "string(none)",
            }
        },
    )
    padding: Optional[float] = Field(
        default=None,
        description="""The padding between the border and content of the legend group in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "padding", "domain_of": ["Legend", "ViewConfiguration"]}},
    )
    fill: str = Field(
        default=...,
        description="""The name of a scale that maps to a fill color. This represents the color used to visualize discrete classes
or continuous data in the legend.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "domain_of": [
                    "Legend",
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["Legend", "LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
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
        json_schema_extra={
            "linkml_meta": {"alias": "labelColor", "domain_of": ["Axis", "Legend"], "slot_uri": "rgbHexSlot"}
        },
    )
    labelOpacity: str = Field(
        default=...,
        description="""The opacity of legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelOpacity", "domain_of": ["Axis", "Legend"], "slot_uri": "opacityValueSlot"}
        },
    )
    labelFont: Optional[str] = Field(
        default="Arial",
        description="""Font name for legend labels.""",
        json_schema_extra={
            "linkml_meta": {"alias": "labelFont", "domain_of": ["Axis", "Legend"], "ifabsent": "string(Arial)"}
        },
    )
    labelFontSize: float = Field(
        default=...,
        description="""Font size in pixels for legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontSize", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontStyle: FontStyleEnum = Field(
        default=...,
        description="""Font style of legend labels""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontStyle", "domain_of": ["Axis", "Legend"]}},
    )
    labelFontWeight: FontWeightEnum = Field(
        default=...,
        description="""Font weight of legend labels.""",
        json_schema_extra={"linkml_meta": {"alias": "labelFontWeight", "domain_of": ["Axis", "Legend"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
            }
        },
    )


class FontSizeItem(ConfiguredBaseModel):
    """
    Fontsize of text in pixels.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: float = Field(
        default=...,
        description="""Font size value.""",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
        json_schema_extra={"linkml_meta": {"alias": "orient", "domain_of": ["Axis", "Legend", "Title"]}},
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
    fontSize: float = Field(
        default=...,
        description="""Font size in pixels of the title text.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"alias": "fontSize", "domain_of": ["Title", "TextEncodeEnter"]}},
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
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["Axis", "ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: str = Field(
        default=...,
        description="""The value or field to which to apply the color.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": [
                    "AggregateTransform",
                    "SpreadTransform",
                    "ContinuousColorDomain",
                    "ColorItem",
                    "AxisItem",
                    "ConditionalFillUpdate",
                ],
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
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
            "linkml_meta": {"alias": "scale", "domain_of": ["Axis", "ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: AxisEnum = Field(
        default=...,
        description="""The mark's field value transformed by the scale. Either x or y.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": [
                    "AggregateTransform",
                    "SpreadTransform",
                    "ContinuousColorDomain",
                    "ColorItem",
                    "AxisItem",
                    "ConditionalFillUpdate",
                ],
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
            }
        },
    )


class HorizontalAlignObject(ConfiguredBaseModel):
    """
    Object indicating the horizontal alignment.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: HorizontalAlignEnum = Field(
        default=...,
        description="""The actual value for alignment.""",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
            }
        },
    )


class BaseLineObject(ConfiguredBaseModel):
    """
    The vertical alignment of the text relative to its y-coordinate.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: BaseLineEnum = Field(
        default=...,
        description="""The actual value for vertical alignment.""",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
            }
        },
    )


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

    opacity: Optional[OpacityObject] = Field(
        default=None,
        description="""The opacity of the image mark.""",
        json_schema_extra={"linkml_meta": {"alias": "opacity", "domain_of": ["ImageEncodeEnter"]}},
    )
    fill: list[ColorItem] = Field(
        default=...,
        description="""The colormap by which to show the intensity value of the image or channel.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "domain_of": [
                    "Legend",
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "stroke",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
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
                    "Legend",
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
    fillOpacity: OpacityObject = Field(
        default=...,
        description="""Opacity value for the label fill between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
            }
        },
    )
    strokeOpacity: OpacityObject = Field(
        default=...,
        description="""Opacity value for the label stroke between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
    )
    strokeWidth: PositiveFloatObject = Field(
        default=...,
        description="""The width of the label outlines in pixels.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["Legend", "LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
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
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
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
                    "Legend",
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
    fillOpacity: OpacityObject = Field(
        default=...,
        description="""Opacity value for the point fill between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
            }
        },
    )
    strokeOpacity: Optional[OpacityObject] = Field(
        default=None,
        description="""Opacity value for the point outlines between 0 and 1.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
    )
    strokeWidth: Optional[PositiveFloatObject] = Field(
        default=None,
        description="""The width of the point outlines in pixels.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["Legend", "LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
    )
    size: PositiveFloatObject = Field(
        default=...,
        description="""The points bounding box area size (typographic points are 1/72 in.).""",
        json_schema_extra={"linkml_meta": {"alias": "size", "domain_of": ["PointsEncodeEnter"]}},
    )
    shape: CircleShapeObject = Field(
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
                    "Legend",
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
    fillOpacity: OpacityObject = Field(
        default=...,
        description="""The fill opacity of the individual shape geometries.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
            }
        },
    )
    stroke: Optional[RGBHexItem] = Field(
        default=None,
        description="""The color of the shapes outlines as RGB hexstring""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "stroke",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
    )
    strokeWidth: Optional[PositiveFloatObject] = Field(
        default=None,
        description="""The width of the outline in pixels""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeWidth",
                "domain_of": ["Legend", "LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
            }
        },
    )
    strokeOpacity: Optional[OpacityObject] = Field(
        default=None,
        description="""The opacity of the outline of the individual shape geometries.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "strokeOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter"],
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
    align: HorizontalAlignObject = Field(
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
    baseline: BaseLineObject = Field(
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
                    "Legend",
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
    fillOpacity: Optional[OpacityObject] = Field(
        default=None,
        description="""Opacity of the text.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fillOpacity",
                "domain_of": ["LabelEncodeEnter", "PointsEncodeEnter", "PathEncodeEnter", "TextEncodeEnter"],
            }
        },
    )


class GroupEncodeEnter(ConfiguredBaseModel):
    """
    Encoding for the position, width and height of a group mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    x: PositiveFloatObject = Field(
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
    y: PositiveFloatObject = Field(
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
    width: PositiveFloatObject = Field(
        default=...,
        description="""The width of the mark in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "width", "domain_of": ["GroupEncodeEnter", "ViewConfiguration"]}},
    )
    height: PositiveFloatObject = Field(
        default=...,
        description="""The height of the mark in pixels.""",
        json_schema_extra={"linkml_meta": {"alias": "height", "domain_of": ["GroupEncodeEnter", "ViewConfiguration"]}},
    )


class MarkEncodeUpdate(ConfiguredBaseModel):
    """
    Update properties that are evaluated for all existing (non-exiting) mark instances.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    fill: Optional[list[Union[ConditionalColorUpdate, ConditionalFillUpdate, NAColorUpdate, RGBHexItem]]] = Field(
        default=None,
        description="""Update of fill color based on a test condition and optional a backup static fill value""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "fill",
                "any_of": [
                    {"range": "ConditionalFillUpdate"},
                    {"range": "RGBHexItem"},
                    {"range": "NAColorUpdate"},
                    {"range": "ConditionalColorUpdate"},
                ],
                "domain_of": [
                    "Legend",
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
        json_schema_extra={
            "linkml_meta": {
                "alias": "test",
                "domain_of": ["ConditionalFillUpdate", "NAColorUpdate", "ConditionalColorUpdate"],
            }
        },
    )
    scale: str = Field(
        default=...,
        description="""The scale to use for applying the fill color. This scale MUST exist in the view configuration Scales array.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scale", "domain_of": ["Axis", "ColorItem", "AxisItem", "ConditionalFillUpdate"]}
        },
    )
    field: str = Field(
        default=...,
        description="""The column that serves as data input, in the test condition this corresponds to 'datum'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "field",
                "domain_of": [
                    "AggregateTransform",
                    "SpreadTransform",
                    "ContinuousColorDomain",
                    "ColorItem",
                    "AxisItem",
                    "ConditionalFillUpdate",
                ],
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


class NAColorUpdate(ConfiguredBaseModel):
    """
    Update the color of a mark glyph if its value is not valid.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    test: str = Field(
        default=...,
        description="""The condition to test on, e.g. '!isValid(datum.value). MUST be a negating is valid expression in Vega. 
See also: https://vega.github.io/vega/docs/expressions/ and it MUST evaluate to either 'true' or 'false'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "test",
                "domain_of": ["ConditionalFillUpdate", "NAColorUpdate", "ConditionalColorUpdate"],
            }
        },
    )
    value: str = Field(
        default=...,
        description="""The color as RGB hex string.""",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
            }
        },
    )

    @field_validator("test")
    def pattern_test(cls, v):
        pattern = re.compile(r"!isValid\([^)]*\)")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid test format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid test format: {v}"
            raise ValueError(err_msg)
        return v

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


class ConditionalColorUpdate(ConfiguredBaseModel):
    """
    Update the color if a value is above or below a given threshold.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/encode"})

    test: str = Field(
        default=...,
        description="""The condition to test on, e.g. 'datum.instance_id) < 3.0'. MUST be an expression starting with 
datum.<column_name> then a space followed by <=,>=,< or> a space again and then any float or integer value.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "test",
                "domain_of": ["ConditionalFillUpdate", "NAColorUpdate", "ConditionalColorUpdate"],
            }
        },
    )
    value: str = Field(
        default=...,
        description="""The color as RGB hex string.""",
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
                    "HorizontalAlignObject",
                    "BaseLineObject",
                    "NAColorUpdate",
                    "ConditionalColorUpdate",
                ],
            }
        },
    )

    @field_validator("test")
    def pattern_test(cls, v):
        pattern = re.compile(r"^datum\.[A-Za-z_][A-Za-z0-9_]*\s*(?:<=|>=|<|>)\s*-?\d+(?:\.\d+)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid test format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid test format: {v}"
            raise ValueError(err_msg)
        return v

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
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["LookupTransform", "Mark"]}},
    )
    encode: str = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of mark instances. In Vega, 
there are three primary property sets: enter, update, exit. The enter properties are evaluated when data is 
processed for the first time and a mark instance is newly added to a scene. The update properties are 
evaluated for all existing (non-exiting) mark instances. The exit properties are evaluated when the data 
backing a mark is removed, and so the mark is leaving the visual scene. However, in this specification we 
currently only support enter and update property sets.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
    )


class MarkDataSource(ConfiguredBaseModel):
    """
    Object with a data field pointing to the name of the datastream that serves as data source for the mark.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    data: str = Field(
        default=...,
        description="""name of the datastream""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": ["ContinuousColorDomain", "MarkDataSource", "ViewConfiguration"],
            }
        },
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
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "raster_image",
                "ifabsent": "string(raster_image)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["LookupTransform", "Mark"]}},
    )
    encode: ImageEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the raster_image mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "raster_label",
                "ifabsent": "string(raster_label)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["LookupTransform", "Mark"]}},
    )
    encode: LabelEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the raster_image mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "symbol",
                "ifabsent": "string(symbol)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["LookupTransform", "Mark"]}},
    )
    encode: SymbolEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the symbol mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
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
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "path",
                "ifabsent": "string(path)",
            }
        },
    )
    from_: MarkDataSource = Field(
        default=...,
        description="""The data stream used as the source for the graphical mark.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["LookupTransform", "Mark"]}},
    )
    encode: PathEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position and appearance of the symbol mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
    )


class TextMark(ConfiguredBaseModel):
    """
    Text marks can be used to annotate data and provide labels and titles for axes and legends.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    type: Optional[Literal["text"]] = Field(
        default="text",
        description="""The type of the mark. In this case, it is always 'text'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "text",
                "ifabsent": "string(text)",
            }
        },
    )
    encode: Optional[TextEncode] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    zindex: int = Field(
        default=...,
        description="""An integer z-index indicating the layering order of sibling mark items. The default value is 0. Higher values 
(1) will cause marks to be drawn on top of those with lower z-index values.""",
        json_schema_extra={"linkml_meta": {"alias": "zindex", "domain_of": ["Axis", "Legend", "Mark", "TextMark"]}},
    )


class GroupMark(ConfiguredBaseModel):
    """
    Group marks are containers for other marks, and used to create visualizations with multiple views or layers. Each
    group instance recursively defines its own nested visualization specification. Group marks provide their own
    coordinate space and can include nested data, signal, scale, axis, legend, title and mark definitions.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    type: Optional[Literal["group"]] = Field(
        default="group",
        description="""The type of the mark. In this case, it is always 'group'.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "BaseFormat", "Scale", "Legend", "Mark", "TextMark", "GroupMark"],
                "equals_string": "group",
                "ifabsent": "string(group)",
            }
        },
    )
    encode: GroupEncode = Field(
        default=...,
        description="""A set of visual encoding properties that determine the position of the group mark.""",
        json_schema_extra={"linkml_meta": {"alias": "encode", "domain_of": ["Mark", "TextMark", "GroupMark"]}},
    )
    scales: list[str] = Field(
        default=...,
        description="""Scales map data values (numbers, dates, categories, etc.) to visual values (pixels, colors, sizes). 
Scales are a fundamental building block of data visualization, as they determine the nature of visual 
encodings.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scales", "domain_of": ["BaseScales", "GroupMark", "ViewConfiguration"]}
        },
    )
    axes: list[Axis] = Field(
        default=...,
        description="""Axes visualize spatial scale mappings using ticks, grid lines and labels.""",
        json_schema_extra={"linkml_meta": {"alias": "axes", "domain_of": ["GroupMark", "ViewConfiguration"]}},
    )
    legends: Optional[list[Legend]] = Field(
        default=None,
        description="""Legends visualize scale mappings for visual values such as color, shape and size.""",
        json_schema_extra={"linkml_meta": {"alias": "legends", "domain_of": ["GroupMark", "ViewConfiguration"]}},
    )
    marks: list[Mark] = Field(
        default=...,
        description="""Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting 
symbols. Marks are the basic visual building block of a visualization, providing basic shapes whose 
properties can be set according to backing data. Mark property definitions may be simple constants or data 
fields, or scales can be used to map data values to visual values.""",
        json_schema_extra={"linkml_meta": {"alias": "marks", "domain_of": ["GroupMark", "ViewConfiguration"]}},
    )


class ViewConfiguration(ConfiguredBaseModel):
    """
    Viewconfiguration based on vega for the scverse visualization ecosystem. Currently, only supports SpatialData.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/scverse/vega-scverse/specification"}
    )

    height: int = Field(
        default=...,
        description="""The height of the plotting area. The plotting area is defined as the rectangular region within a visualization 
where graphical marks (such as points, lines, or bars) are rendered, bounded by the axes and padding, 
excluding titles, legends, and margins.""",
        json_schema_extra={"linkml_meta": {"alias": "height", "domain_of": ["GroupEncodeEnter", "ViewConfiguration"]}},
    )
    width: int = Field(
        default=...,
        description="""The width of the plotting area. The plotting area is defined as the rectangular region within a visualization 
where graphical marks (such as points, lines, or bars) are rendered, bounded by the axes and padding, 
excluding titles, legends, and margins.""",
        json_schema_extra={"linkml_meta": {"alias": "width", "domain_of": ["GroupEncodeEnter", "ViewConfiguration"]}},
    )
    padding: Optional[Union[Padding, float]] = Field(
        default=None,
        description="""padding defines the amount of space (in pixels) to reserve between the edge of the chart container and the inner 
view area where data marks are rendered. It acts as an internal margin that ensures visual elements like axes, 
titles, and legends don't touch or overflow the chart's outer boundaries.
When combined with \"autosize\": {\"type\": \"fit\", \"contains\": \"padding\"}, this padding is included within the chart's 
specified width and height, and the inner view is resized accordingly to preserve layout integrity. If padding
is defined with this class. This class should at least have one attribute defined.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "padding",
                "any_of": [{"range": "float"}, {"range": "Padding"}],
                "domain_of": ["Legend", "ViewConfiguration"],
            }
        },
    )
    title: Optional[Title] = Field(
        default=None,
        description="""The title directive adds a descriptive title to a chart.""",
        json_schema_extra={"linkml_meta": {"alias": "title", "domain_of": ["ViewConfiguration"]}},
    )
    data: list[DataObject] = Field(
        default=...,
        description="""Scverse data set definitions and transforms define the data to load and how to process it.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": ["ContinuousColorDomain", "MarkDataSource", "ViewConfiguration"],
            }
        },
    )
    scales: Optional[BaseScales] = Field(
        default=None,
        description="""Scales map data values (numbers, dates, categories, etc.) to visual values (pixels, colors, sizes). 
Scales are a fundamental building block of data visualization, as they determine the nature of visual 
encodings.""",
        json_schema_extra={
            "linkml_meta": {"alias": "scales", "domain_of": ["BaseScales", "GroupMark", "ViewConfiguration"]}
        },
    )
    axes: Optional[list[Axis]] = Field(
        default=None,
        description="""Axes visualize spatial scale mappings using ticks, grid lines and labels.""",
        json_schema_extra={"linkml_meta": {"alias": "axes", "domain_of": ["GroupMark", "ViewConfiguration"]}},
    )
    legends: Optional[list[Legend]] = Field(
        default=None,
        description="""Legends visualize scale mappings for visual values such as color, shape and size.""",
        json_schema_extra={"linkml_meta": {"alias": "legends", "domain_of": ["GroupMark", "ViewConfiguration"]}},
    )
    marks: list[Union[GroupMark, Mark]] = Field(
        default=...,
        description="""Graphical marks visually encode data using geometric primitives such as rectangles, lines, and plotting 
symbols. Marks are the basic visual building block of a visualization, providing basic shapes whose 
properties can be set according to backing data. Mark property definitions may be simple constants or data 
fields, or scales can be used to map data values to visual values.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "marks",
                "any_of": [{"range": "Mark"}, {"range": "GroupMark"}],
                "domain_of": ["GroupMark", "ViewConfiguration"],
            }
        },
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
DataObject.model_rebuild()
SpatialDataObject.model_rebuild()
BaseTableObject.model_rebuild()
SpatialDataElementObject.model_rebuild()
Transform.model_rebuild()
FilterTransform.model_rebuild()
FilterChannelTransform.model_rebuild()
LookupTransform.model_rebuild()
AggregateTransform.model_rebuild()
SpreadTransform.model_rebuild()
NormalizationFormulaTransform.model_rebuild()
BaseFormat.model_rebuild()
SpatialDataFormat.model_rebuild()
ElementFormat.model_rebuild()
BaseScales.model_rebuild()
Scale.model_rebuild()
BaseAxisScale.model_rebuild()
ColorScale.model_rebuild()
LinearColorScale.model_rebuild()
BaseCategoricalColorScale.model_rebuild()
ContinuousColorDomain.model_rebuild()
ContinuousColorMapRange.model_rebuild()
Axis.model_rebuild()
Legend.model_rebuild()
CategoricalLegend.model_rebuild()
ColorBarLegend.model_rebuild()
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
HorizontalAlignObject.model_rebuild()
BaseLineObject.model_rebuild()
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
NAColorUpdate.model_rebuild()
ConditionalColorUpdate.model_rebuild()
Mark.model_rebuild()
MarkDataSource.model_rebuild()
RasterImageMark.model_rebuild()
RasterLabelMark.model_rebuild()
PointsMark.model_rebuild()
ShapesMark.model_rebuild()
TextMark.model_rebuild()
GroupMark.model_rebuild()
ViewConfiguration.model_rebuild()

