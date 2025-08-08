

# Slot: domain 



URI: [vega_scverse:domain](https://w3id.org/scverse/vega-scverse/domain)
Alias: domain

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BaseAxisScale](BaseAxisScale.md) | A vega like scale specifically for mapping from a data domain to an axis rang... |  no  |
| [LinearColorScale](LinearColorScale.md) | A vega like scale specifically for mapping from a linear continuous data doma... |  no  |
| [BaseCategoricalColorScale](BaseCategoricalColorScale.md) | A scale to map a discrete data domain to discrete colors |  no  |
| [Axis](Axis.md) | An axis visualizes a spatial scale mapping for cartesian coordinates using ti... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:domain |
| native | vega_scverse:domain |




## LinkML Source

<details>
```yaml
name: domain
alias: domain
domain_of:
- BaseAxisScale
- LinearColorScale
- BaseCategoricalColorScale
- Axis
range: string

```
</details>