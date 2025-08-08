# Enum: CapEnum 




_The style of the stroke end for axis tick marks._



URI: [CapEnum](CapEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| butt | None | The line ends exactly at its endpoint, producing a flat, squared-off edge per... |
| round | None | The line ends with a semi-circular extension beyond its endpoint, creating a ... |
| square | None | The line ends with a square extension beyond its endpoint |




## Slots

| Name | Description |
| ---  | --- |
| [gridCap](gridCap.md) | The stroke cap for axis grid lines |
| [tickCap](tickCap.md) | The stroke cap for axis tick marks |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification






## LinkML Source

<details>
```yaml
name: CapEnum
description: The style of the stroke end for axis tick marks.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
permissible_values:
  butt:
    text: butt
    description: "The line ends exactly at its endpoint, producing a flat, squared-off\
      \ edge perpendicular to the path. \nThere is no extension beyond the endpoint."
  round:
    text: round
    description: "The line ends with a semi-circular extension beyond its endpoint,\
      \ creating a rounded cap with a radius equal to \nhalf the line's thickness.\
      \ This softens sharp edges and creates smooth joins."
  square:
    text: square
    description: "The line ends with a square extension beyond its endpoint. It is\
      \ similar to butt but extends the line slightly \npast the endpoint, by half\
      \ the line's thickness, resulting in a squared-off cap that projects outward."

```
</details>
