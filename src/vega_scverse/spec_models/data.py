from pydantic import field_validator

from .linkml_data import BaseTableObject


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
