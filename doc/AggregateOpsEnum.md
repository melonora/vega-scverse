# Enum: AggregateOpsEnum 




_The summary statistic to apply for an aggregation transform. The summary statistic is calculated per datashade_

_raster pixel._



URI: [AggregateOpsEnum](AggregateOpsEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| any | None |  |
| max | None | Maximum value of all elements in each datashade raster pixel |
| min | None | Minimum value of all elements in each datashade raster pixel |
| mean | None | Mean value of all elements in each datashade raster pixel |
| stdev | None | Standard deviation of all elements in each datashade raster pixel |
| sum | None | Sum of all elements in each datashade raster pixel |
| variance | None | Variance of all elements in each datashade raster pixel |
| count | None | Count elements each datashade raster pixel, returning the result as a uint32,... |




## Slots

| Name | Description |
| ---  | --- |
| [ops](ops.md) | The summary statistic to apply per field |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification






## LinkML Source

<details>
```yaml
name: AggregateOpsEnum
description: 'The summary statistic to apply for an aggregation transform. The summary
  statistic is calculated per datashade

  raster pixel.'
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
permissible_values:
  any:
    text: any
  max:
    text: max
    description: Maximum value of all elements in each datashade raster pixel.
  min:
    text: min
    description: Minimum value of all elements in each datashade raster pixel.
  mean:
    text: mean
    description: Mean value of all elements in each datashade raster pixel.
  stdev:
    text: stdev
    description: Standard deviation of all elements in each datashade raster pixel.
  sum:
    text: sum
    description: Sum of all elements in each datashade raster pixel
  variance:
    text: variance
    description: Variance of all elements in each datashade raster pixel.
  count:
    text: count
    description: "Count elements each datashade raster pixel, returning the result\
      \ as a uint32, or a float32 if using \nantialiasing."

```
</details>
