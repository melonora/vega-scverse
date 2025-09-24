from typing import Union

from pydantic import field_validator
from pydantic import Field
from .linkml_data import BaseTableObject, BaseLookupTransform, BaseSpreadTransform, BaseNormalizationFormulaTransform, \
    BaseAggregateTransform, BaseSpatialDataElementObject, FilterChannelTransform, FilterTransform


class TableObject(BaseTableObject):
    @field_validator('transform')
    def transform_length(cls, v):
        """Ensure only a single transform object is present."""
        if (length := len(v)) != 1:
            err_msg = f"The transform array of a `TableObject` must be of length 1, but is of length: {length} "
            raise ValueError(err_msg)
        return v

    @field_validator('transform')
    def transform_filter_element(cls, v):
        """Ensure single transform has type `filter_element`."""
        if v[0].type != "filter_element":
            raise ValueError(f"The transform of an `TableObject` must be of type `filter_element`, got {v[0].type}")
        return v


class LookupTransform(BaseLookupTransform):
    from_: str = Field(
        default=...,
        alias="from",
        description="""The name of the secondary data stream upon which to perform the lookup.""",
        json_schema_extra={"linkml_meta": {"alias": "from_", "domain_of": ["BaseLookupTransform"]}},
    )
    as_: list[str] = Field(
        default=...,
        description="""To be added""",
        alias="as",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "BaseLookupTransform",
                    "BaseAggregateTransform",
                    "BaseSpreadTransform",
                    "BaseNormalizationFormulaTransform",
                ],
            }
        },
    )


class SpreadTransform(BaseSpreadTransform):
    as_: list[str] = Field(
        default=...,
        description="""To be added""",
        alias="as",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "BaseLookupTransform",
                    "BaseAggregateTransform",
                    "BaseSpreadTransform",
                    "BaseNormalizationFormulaTransform",
                ],
            }
        },
    )


class NormalizationFormulaTransform(BaseNormalizationFormulaTransform):
    as_: str = Field(
        default=...,
        description="""To be added""",
        alias="as",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "BaseLookupTransform",
                    "BaseAggregateTransform",
                    "BaseSpreadTransform",
                    "BaseNormalizationFormulaTransform",
                ],
            }
        },
    )


class AggregateTransform(BaseAggregateTransform):
    as_: list[str] = Field(
        default=...,
        description="""To be added""",
        alias="as",
        json_schema_extra={
            "linkml_meta": {
                "alias": "as_",
                "domain_of": [
                    "BaseLookupTransform",
                    "BaseAggregateTransform",
                    "BaseSpreadTransform",
                    "BaseNormalizationFormulaTransform",
                ],
            }
        },
    )


class SpatialDataElementObject(BaseSpatialDataElementObject):
    transform: list[
        Union[
            AggregateTransform,
            LookupTransform,
            NormalizationFormulaTransform,
            SpreadTransform,
            FilterChannelTransform,
            FilterTransform,
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
                    {"range": "BaseLookupTransform"},
                    {"range": "FilterTransform"},
                    {"range": "FilterChannelTransform"},
                    {"range": "BaseAggregateTransform"},
                    {"range": "BaseSpreadTransform"},
                    {"range": "BaseNormalizationFormulaTransform"},
                ],
                "domain_of": ["BaseTableObject", "BaseSpatialDataElementObject"],
            }
        },
    )