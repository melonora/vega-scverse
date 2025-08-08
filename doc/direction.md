

# Slot: direction 


_The direction of the legend, one of 'vertical' or 'horizontal'._





URI: [vega_scverse:direction](https://w3id.org/scverse/vega-scverse/direction)
Alias: direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ColorBarLegend](ColorBarLegend.md) | Type of legend for continuous data |  no  |
| [CategoricalLegend](CategoricalLegend.md) | Type of legend for categorical data |  no  |
| [Legend](Legend.md) | Vega like configuration for specifying legends in the SpatialData visualizati... |  no  |







## Properties

* Range: [LegendDirections](LegendDirections.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:direction |
| native | vega_scverse:direction |




## LinkML Source

<details>
```yaml
name: direction
description: The direction of the legend, one of 'vertical' or 'horizontal'.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: direction
owner: Legend
domain_of:
- Legend
range: legendDirections
required: true

```
</details>