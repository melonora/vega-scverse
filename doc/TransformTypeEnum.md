# Enum: TransformTypeEnum 




_Valid transforms on a data stream within a scverse viewconfig._



URI: [TransformTypeEnum](TransformTypeEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| filter_element | None | Filter an element from a root data object, like a SpatialData zarr |
| filter_cs | None | Filter the coordinate systems of an element to point to coordinate system the... |
| filter_scale | None | Filter on a particular scale in multiscale raster data |
| filter_channel | None | Filter on a particular channel in raster data |
| aggregate | None | Group and summarize an input data stream to produce a derived output stream |
| spread | None | Expand each pixel in a rasterized image by a specified number of pixels to ma... |
| lookup | None | Extend a primary data stream by looking up values on a secondary data stream |
| formula | None | Apply a formula to a data input stream |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | The type of transform |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification






## LinkML Source

<details>
```yaml
name: TransformTypeEnum
description: Valid transforms on a data stream within a scverse viewconfig.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
permissible_values:
  filter_element:
    text: filter_element
    description: Filter an element from a root data object, like a SpatialData zarr.
  filter_cs:
    text: filter_cs
    description: Filter the coordinate systems of an element to point to coordinate
      system the element is displayed in.
  filter_scale:
    text: filter_scale
    description: Filter on a particular scale in multiscale raster data.
  filter_channel:
    text: filter_channel
    description: Filter on a particular channel in raster data.
  aggregate:
    text: aggregate
    description: Group and summarize an input data stream to produce a derived output
      stream.
  spread:
    text: spread
    description: Expand each pixel in a rasterized image by a specified number of
      pixels to make sparse data more visible.
  lookup:
    text: lookup
    description: Extend a primary data stream by looking up values on a secondary
      data stream.
  formula:
    text: formula
    description: Apply a formula to a data input stream.

```
</details>
