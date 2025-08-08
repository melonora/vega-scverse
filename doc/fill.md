

# Slot: fill 



URI: [vega_scverse:fill](https://w3id.org/scverse/vega-scverse/fill)
Alias: fill

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CategoricalLegend](CategoricalLegend.md) | Type of legend for categorical data |  no  |
| [Legend](Legend.md) | Vega like configuration for specifying legends in the SpatialData visualizati... |  no  |
| [ColorBarLegend](ColorBarLegend.md) | Type of legend for continuous data |  no  |
| [LabelEncodeEnter](LabelEncodeEnter.md) | Enter properties that are evaluated when label data is processed for the firs... |  no  |
| [TextEncodeEnter](TextEncodeEnter.md) | Enter properties that are evaluated when data for a text mark is processed fo... |  no  |
| [PointsEncodeEnter](PointsEncodeEnter.md) | Enter properties that are evaluated when points data is processed for the fir... |  no  |
| [PathEncodeEnter](PathEncodeEnter.md) | Enter properties that are evaluated when shapes data is processed for the fir... |  no  |
| [ImageEncodeEnter](ImageEncodeEnter.md) | Enter properties that are evaluated when image data is processed for the firs... |  no  |
| [MarkEncodeUpdate](MarkEncodeUpdate.md) | Update properties that are evaluated for all existing (non-exiting) mark inst... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:fill |
| native | vega_scverse:fill |




## LinkML Source

<details>
```yaml
name: fill
alias: fill
domain_of:
- Legend
- ImageEncodeEnter
- LabelEncodeEnter
- PointsEncodeEnter
- PathEncodeEnter
- TextEncodeEnter
- MarkEncodeUpdate
range: string

```
</details>