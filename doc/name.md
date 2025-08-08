

# Slot: name 



URI: [vega_scverse:name](https://w3id.org/scverse/vega-scverse/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TableObject](TableObject.md) | AnnData Table object stream |  no  |
| [SpatialDataElementObject](SpatialDataElementObject.md) | Data object pertaining to an element within the SpatialData object |  no  |
| [Scale](Scale.md) | Base class for vega like scales which map from a data domain to a visual rang... |  no  |
| [BaseAxisScale](BaseAxisScale.md) | A vega like scale specifically for mapping from a data domain to an axis rang... |  yes  |
| [SpatialDataObject](SpatialDataObject.md) | SpatialData object specific to the SpatialData root |  no  |
| [BaseCategoricalColorScale](BaseCategoricalColorScale.md) | A scale to map a discrete data domain to discrete colors |  no  |
| [ColorScale](ColorScale.md) | Abstract class to map a data domain to a color range |  yes  |
| [LinearColorScale](LinearColorScale.md) | A vega like scale specifically for mapping from a linear continuous data doma... |  no  |
| [DataObject](DataObject.md) | Abstract class for Vega like data set definitions and transforms that define ... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:name |
| native | vega_scverse:name |




## LinkML Source

<details>
```yaml
name: name
alias: name
domain_of:
- DataObject
- Scale
range: string

```
</details>