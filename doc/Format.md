

# Slot: format 


_Format object containing the type of data as object and a string value representing the version._





URI: [vega_scverse:format](https://w3id.org/scverse/vega-scverse/format)
Alias: format

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TableObject](TableObject.md) | AnnData Table object stream |  no  |
| [SpatialDataObject](SpatialDataObject.md) | SpatialData object specific to the SpatialData root |  no  |
| [DataObject](DataObject.md) | Abstract class for Vega like data set definitions and transforms that define ... |  no  |
| [SpatialDataElementObject](SpatialDataElementObject.md) | Data object pertaining to an element within the SpatialData object |  no  |







## Properties

* Range: [Format](Format.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:format |
| native | vega_scverse:format |




## LinkML Source

<details>
```yaml
name: format
description: Format object containing the type of data as object and a string value
  representing the version.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: format
owner: DataObject
domain_of:
- DataObject
range: Format
required: true

```
</details>