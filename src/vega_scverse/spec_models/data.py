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
        "description": "Vega like specification for the data array used in view "
        "configurations for the scverse visualization ecosystem.",
        "id": "https://w3id.org/scverse/vega-scverse/data",
        "imports": ["linkml:types"],
        "license": "BSD-3",
        "name": "vega-scverse-data",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": "src\\vega_scverse\\schema\\data.yaml",
        "title": "vega-scverse-data",
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
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    format: Format = Field(
        default=...,
        description="""Format object containing the type of data as object and a string value representing the version.""",
        json_schema_extra={"linkml_meta": {"alias": "format", "domain_of": ["DataObject"]}},
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
    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    format: Format = Field(
        default=...,
        description="""Format object containing the type of data as object and a string value representing the version.""",
        json_schema_extra={"linkml_meta": {"alias": "format", "domain_of": ["DataObject"]}},
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


class TableObject(DataObject):
    """
    AnnData Table object stream.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    source: str = Field(
        default=...,
        description="""The source of the SpatialData element. Must be the name / identifier of a SpatialData Object in the 
view configuration.""",
        json_schema_extra={
            "linkml_meta": {"alias": "source", "domain_of": ["TableObject", "SpatialDataElementObject"]}
        },
    )
    transform: list[str] = Field(
        default=...,
        description="""An array containing a single transform 'filter_element' with an expression stating which table to obtain
from the source SpatialData object stream.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "transform",
                "domain_of": ["TableObject", "SpatialDataElementObject"],
                "exactly_one_of": [{"range": "FilterTransform"}],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    format: Format = Field(
        default=...,
        description="""Format object containing the type of data as object and a string value representing the version.""",
        json_schema_extra={"linkml_meta": {"alias": "format", "domain_of": ["DataObject"]}},
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

    source: str = Field(
        default=...,
        description="""The source of the SpatialData element. Must be the name / identifier of a SpatialData Object in the 
view configuration.""",
        json_schema_extra={
            "linkml_meta": {"alias": "source", "domain_of": ["TableObject", "SpatialDataElementObject"]}
        },
    )
    transform: list[
        Union[
            AggregateTransform, FilterChannelTransform, FilterTransform, NormalizationFormulaTransform, SpreadTransform
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
                    {"range": "FilterTransform"},
                    {"range": "FilterChannelTransform"},
                    {"range": "AggregateTransform"},
                    {"range": "SpreadTransform"},
                    {"range": "NormalizationFormulaTransform"},
                ],
                "domain_of": ["TableObject", "SpatialDataElementObject"],
            }
        },
    )
    name: str = Field(
        default=...,
        description="""The name used throughout the view configuration to refer to the data object. It is an arbitrary string 
followed by an underscore and pseudo UUID.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["DataObject"]}},
    )
    format: Format = Field(
        default=...,
        description="""Format object containing the type of data as object and a string value representing the version.""",
        json_schema_extra={"linkml_meta": {"alias": "format", "domain_of": ["DataObject"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Transform", "Format"]}},
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
                "domain_of": ["Transform", "Format"],
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

    expr: list[Union[int, str]] = Field(
        default=...,
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
            "linkml_meta": {"alias": "type", "domain_of": ["Transform", "Format"], "equals_string": "filter_channel"}
        },
    )


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
        json_schema_extra={"linkml_meta": {"alias": "field", "domain_of": ["AggregateTransform", "SpreadTransform"]}},
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
                "domain_of": ["AggregateTransform", "SpreadTransform", "NormalizationFormulaTransform"],
            }
        },
    )
    type: Literal["aggregate"] = Field(
        default="aggregate",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "Format"],
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
        json_schema_extra={"linkml_meta": {"alias": "field", "domain_of": ["AggregateTransform", "SpreadTransform"]}},
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
                "domain_of": ["AggregateTransform", "SpreadTransform", "NormalizationFormulaTransform"],
            }
        },
    )
    type: Literal["spread"] = Field(
        default="spread",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "Format"],
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
                "domain_of": ["AggregateTransform", "SpreadTransform", "NormalizationFormulaTransform"],
            }
        },
    )
    type: Literal["formula"] = Field(
        default="formula",
        description="""The type of transform.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "domain_of": ["Transform", "Format"],
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


class Format(ConfiguredBaseModel):
    """
    Format object containing the type of data as object and a string value representing the version.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/data"})

    type: str = Field(
        default=...,
        description="""The type of the data as string, e.g. RasterFormat""",
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Transform", "Format"]}},
    )
    version: str = Field(
        default=...,
        description="""The version of the data type that is defined. Defined as semantic version + optional development release.""",
        json_schema_extra={"linkml_meta": {"alias": "version", "domain_of": ["Format"]}},
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


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
DataObject.model_rebuild()
SpatialDataObject.model_rebuild()
TableObject.model_rebuild()
SpatialDataElementObject.model_rebuild()
Transform.model_rebuild()
FilterTransform.model_rebuild()
FilterChannelTransform.model_rebuild()
AggregateTransform.model_rebuild()
SpreadTransform.model_rebuild()
NormalizationFormulaTransform.model_rebuild()
Format.model_rebuild()

