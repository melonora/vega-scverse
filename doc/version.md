

# Slot: version 


_The version of the data type that is defined. Defined as semantic version + optional development release._





URI: [vega_scverse:version](https://w3id.org/scverse/vega-scverse/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Format](Format.md) | Format object containing the type of data as object and a string value repres... |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^(\d+\.\d+)(\.\d+)?([a-zA-Z0-9.+-]*)?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:version |
| native | vega_scverse:version |




## LinkML Source

<details>
```yaml
name: version
description: The version of the data type that is defined. Defined as semantic version
  + optional development release.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: version
owner: Format
domain_of:
- Format
range: string
required: true
pattern: ^(\d+\.\d+)(\.\d+)?([a-zA-Z0-9.+-]*)?$

```
</details>