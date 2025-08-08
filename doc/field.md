

# Slot: field 



URI: [vega_scverse:field](https://w3id.org/scverse/vega-scverse/field)
Alias: field

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AxisItem](AxisItem.md) | A axis item which for a mark can define the scale and field used for the axis... |  no  |
| [ColorItem](ColorItem.md) | A single color item definition specifying the scale on which the color is bas... |  no  |
| [ContinuousColorDomain](ContinuousColorDomain.md) | A data domain or source for a LinearColorScale |  no  |
| [SpreadTransform](SpreadTransform.md) | Datashade transform expanding each pixel in a rasterized image by a specified... |  no  |
| [ConditionalFillUpdate](ConditionalFillUpdate.md) | Update color based on test condition |  no  |
| [AggregateTransform](AggregateTransform.md) | Group and summarize an input data stream to produce a derived output stream u... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:field |
| native | vega_scverse:field |




## LinkML Source

<details>
```yaml
name: field
alias: field
domain_of:
- AggregateTransform
- SpreadTransform
- ContinuousColorDomain
- ColorItem
- AxisItem
- ConditionalFillUpdate
range: string

```
</details>