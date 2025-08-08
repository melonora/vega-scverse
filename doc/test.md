

# Slot: test 


_The condition to test on, e.g. 'isValid(datum.value). MUST be a valid expression in Vega. See also:_

_https://vega.github.io/vega/docs/expressions/ and it MUST evaluate to either 'true' or 'false'._





URI: [vega_scverse:test](https://w3id.org/scverse/vega-scverse/test)
Alias: test

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConditionalFillUpdate](ConditionalFillUpdate.md) | Update color based on test condition |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:test |
| native | vega_scverse:test |




## LinkML Source

<details>
```yaml
name: test
description: 'The condition to test on, e.g. ''isValid(datum.value). MUST be a valid
  expression in Vega. See also:

  https://vega.github.io/vega/docs/expressions/ and it MUST evaluate to either ''true''
  or ''false''.'
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
alias: test
owner: ConditionalFillUpdate
domain_of:
- ConditionalFillUpdate
range: string
required: true

```
</details>