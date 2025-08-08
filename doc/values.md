

# Slot: values 


_Explicitly set the visible axis tick and label values. The array entries should be legal values in the _

_backing scale domain._





URI: [vega_scverse:values](https://w3id.org/scverse/vega-scverse/values)
Alias: values

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Axis](Axis.md) | An axis visualizes a spatial scale mapping for cartesian coordinates using ti... |  no  |







## Properties

* Range: [String](String.md)&nbsp;or&nbsp;<br />[Float](Float.md)&nbsp;or&nbsp;<br />[Integer](Integer.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:values |
| native | vega_scverse:values |




## LinkML Source

<details>
```yaml
name: values
description: "Explicitly set the visible axis tick and label values. The array entries\
  \ should be legal values in the \nbacking scale domain."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: values
owner: Axis
domain_of:
- Axis
range: string
required: true
multivalued: true
any_of:
- range: float
- range: integer

```
</details>