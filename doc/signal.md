

# Slot: signal 


_Signal creating random RGB color for labels in a label raster._





URI: [vega_scverse:signal](https://w3id.org/scverse/vega-scverse/signal)
Alias: signal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RandomRGBSignal](RandomRGBSignal.md) | RGB value represented by a hexadecimal string value |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:signal |
| native | vega_scverse:signal |




## LinkML Source

<details>
```yaml
name: signal
description: Signal creating random RGB color for labels in a label raster.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
ifabsent: string(rgb(random()*255, random()*255, random()*255))
alias: signal
owner: RandomRGBSignal
domain_of:
- RandomRGBSignal
range: string
equals_string: rgb(random()*255, random()*255, random()*255)

```
</details>