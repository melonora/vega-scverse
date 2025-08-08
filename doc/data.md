

# Slot: data 



URI: [vega_scverse:data](https://w3id.org/scverse/vega-scverse/data)
Alias: data

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MarkDataSource](MarkDataSource.md) | Object with a data field pointing to the name of the datastream that serves a... |  no  |
| [ViewConfiguration](ViewConfiguration.md) | Viewconfiguration based on vega for the scverse visualization ecosystem |  no  |
| [ContinuousColorDomain](ContinuousColorDomain.md) | A data domain or source for a LinearColorScale |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:data |
| native | vega_scverse:data |




## LinkML Source

<details>
```yaml
name: data
alias: data
domain_of:
- ViewConfiguration
- ContinuousColorDomain
- MarkDataSource
range: string

```
</details>