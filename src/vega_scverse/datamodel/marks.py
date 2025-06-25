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
        "description": "Vega like specification for the marks used in view "
        "configurations for the scverse visualization ecosystem.",
        "id": "https://w3id.org/scverse/vega-scverse/marks",
        "imports": ["linkml:types", "encode"],
        "license": "BSD-3",
        "name": "vega-scverse-marks",
        "prefixes": {
            "linkml": {"prefix_prefix": "linkml", "prefix_reference": "https://w3id.org/linkml/"},
            "orcid": {"prefix_prefix": "orcid", "prefix_reference": "https://orcid.org/"},
            "vega_scverse": {
                "prefix_prefix": "vega_scverse",
                "prefix_reference": "https://w3id.org/scverse/vega-scverse/",
            },
        },
        "see_also": ["https://scverse.github.io/vega-scverse"],
        "source_file": ".\\marks.yaml",
        "title": "vega-scverse-marks",
    }
)


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


class Value(ConfiguredBaseModel):
    """
    Represents either a literal value or a signal-based dynamic value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://w3id.org/scverse/vega-scverse/marks"}
    )

    value: Optional[float] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "ColorItem"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "ColorItem"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "ColorItem"]}},
    )


class RGBHex(ConfiguredBaseModel):
    """
    RGB value represented by a hexadecimal string value.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/marks"})

    value: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "ColorItem"]}},
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


class ColorItem(ConfiguredBaseModel):
    """
    A single color item definition specifying the scale on which the color is based and the value / field
    to which to apply the color.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "https://w3id.org/scverse/vega-scverse/slots"})

    scale: str = Field(
        default=...,
        description="""The color scale.""",
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "ConditionalFillUpdate"]}},
    )
    value: str = Field(
        default=...,
        description="""The value or field to which to apply the color.""",
        json_schema_extra={"linkml_meta": {"alias": "value", "domain_of": ["Value", "RGBHex", "ColorItem"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "enter", "domain_of": ["ImageEncode", "LabelEncode"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "enter", "domain_of": ["ImageEncode", "LabelEncode"]}},
    )
    update: Optional[LabelEncodeUpdate] = Field(
        default=None,
        description="""Enter properties that are evaluated when label data is processed for the first time and the raster_label mark 
is newly added to a scene. Typically included when no random coloring is being used for the labels.""",
        json_schema_extra={"linkml_meta": {"alias": "update", "domain_of": ["LabelEncode"]}},
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
            "linkml_meta": {"alias": "fill", "domain_of": ["ImageEncodeEnter", "LabelEncodeEnter", "LabelEncodeUpdate"]}
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
        json_schema_extra={"linkml_meta": {"alias": "stroke", "domain_of": ["LabelEncodeEnter"]}},
    )
    fill: list[ColorItem] = Field(
        default=...,
        description="""The color fill of each individual label.""",
        min_length=1,
        max_length=1,
        json_schema_extra={
            "linkml_meta": {"alias": "fill", "domain_of": ["ImageEncodeEnter", "LabelEncodeEnter", "LabelEncodeUpdate"]}
        },
    )
    fillOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {"alias": "fillOpacity", "domain_of": ["LabelEncodeEnter"], "slot_uri": "fillOpacity"}
        },
    )
    strokeOpacity: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {"alias": "strokeOpacity", "domain_of": ["LabelEncodeEnter"], "slot_uri": "strokeOpacity"}
        },
    )
    strokeWidth: str = Field(
        default=...,
        json_schema_extra={
            "linkml_meta": {"alias": "strokeWidth", "domain_of": ["LabelEncodeEnter"], "slot_uri": "strokeWidth"}
        },
    )


class LabelEncodeUpdate(ConfiguredBaseModel):
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
                "domain_of": ["ImageEncodeEnter", "LabelEncodeEnter", "LabelEncodeUpdate"],
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
        json_schema_extra={"linkml_meta": {"alias": "scale", "domain_of": ["ColorItem", "ConditionalFillUpdate"]}},
    )
    field: str = Field(
        default=...,
        description="""The column that serves as data input, in the test condition this corresponds to 'datum'.""",
        json_schema_extra={"linkml_meta": {"alias": "field", "domain_of": ["ConditionalFillUpdate"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "type", "domain_of": ["Mark"]}},
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
        json_schema_extra={"linkml_meta": {"alias": "data", "domain_of": ["MarkDataSource"]}},
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
                "domain_of": ["Mark"],
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
                "domain_of": ["Mark"],
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


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Value.model_rebuild()
OpacityValue.model_rebuild()
PositiveValue.model_rebuild()
RGBHex.model_rebuild()
ColorItem.model_rebuild()
ImageEncode.model_rebuild()
LabelEncode.model_rebuild()
ImageEncodeEnter.model_rebuild()
LabelEncodeEnter.model_rebuild()
LabelEncodeUpdate.model_rebuild()
ConditionalFillUpdate.model_rebuild()
Mark.model_rebuild()
MarkDataSource.model_rebuild()
RasterImageMark.model_rebuild()
RasterLabelMark.model_rebuild()

