

# Slot: ops 


_The summary statistic to apply per field. This deviates from vega where ops has a single string value_

_while here it is an array with a length equal to 'field' and 'as'._





URI: [vega_scverse:ops](https://w3id.org/scverse/vega-scverse/ops)
Alias: ops

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AggregateTransform](AggregateTransform.md) | Group and summarize an input data stream to produce a derived output stream u... |  no  |







## Properties

* Range: [AggregateOpsEnum](AggregateOpsEnum.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:ops |
| native | vega_scverse:ops |




## LinkML Source

<details>
```yaml
name: ops
description: 'The summary statistic to apply per field. This deviates from vega where
  ops has a single string value

  while here it is an array with a length equal to ''field'' and ''as''.'
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: ops
owner: AggregateTransform
domain_of:
- AggregateTransform
range: AggregateOpsEnum
required: true
multivalued: true

```
</details>