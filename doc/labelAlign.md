

# Slot: labelAlign 


_Horizontal text alignment for legend labels. In short this means where the label text is relative to the_

_anchor point of the labels (this could be defined as the coordinates where the labels are specified to be)._





URI: [vega_scverse:labelAlign](https://w3id.org/scverse/vega-scverse/labelAlign)
Alias: labelAlign

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ColorBarLegend](ColorBarLegend.md) | Type of legend for continuous data |  no  |
| [CategoricalLegend](CategoricalLegend.md) | Type of legend for categorical data |  no  |
| [Legend](Legend.md) | Vega like configuration for specifying legends in the SpatialData visualizati... |  no  |







## Properties

* Range: [HorizontalAlignEnum](HorizontalAlignEnum.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:labelAlign |
| native | vega_scverse:labelAlign |




## LinkML Source

<details>
```yaml
name: labelAlign
description: 'Horizontal text alignment for legend labels. In short this means where
  the label text is relative to the

  anchor point of the labels (this could be defined as the coordinates where the labels
  are specified to be).'
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: labelAlign
owner: Legend
domain_of:
- Legend
range: HorizontalAlignEnum
required: true

```
</details>