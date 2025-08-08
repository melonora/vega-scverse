

# Slot: expr 



URI: [vega_scverse:expr](https://w3id.org/scverse/vega-scverse/expr)
Alias: expr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FilterChannelTransform](FilterChannelTransform.md) | Filter on particular channels in a raster data object |  no  |
| [FilterTransform](FilterTransform.md) | Select objects from a data stream to keep based on a filter expression |  no  |
| [NormalizationFormulaTransform](NormalizationFormulaTransform.md) | A formula to transform data |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:expr |
| native | vega_scverse:expr |




## LinkML Source

<details>
```yaml
name: expr
alias: expr
domain_of:
- FilterTransform
- FilterChannelTransform
- NormalizationFormulaTransform
range: string

```
</details>