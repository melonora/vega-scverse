# Enum: BaseLineEnum 




_The possible vertical alignments of the text relative to its y-coordinate._

_See the link for an explanation of the meaning of EM square. We do not currently_

_support "line-bottom" and "line-top"._



URI: [BaseLineEnum](BaseLineEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| top | None | The highest part of all characters aligns with the y-coordinate |
| middle | None | The middle of the fonts EM square aligns with the y-coordinate |
| bottom | None | The bottom of all characters combined aligns with the y-coordinate |
| alphabetic | None | aligns the main body of lowercase letters (like a, e, x) so that their base s... |




## Slots

| Name | Description |
| ---  | --- |
| [baseline](baseline.md) | The baseline attribute specifies the vertical alignment (baseline) of the tex... |






## See Also

* [http://designwithfontforge.com/en-US/The_EM_Square.html](http://designwithfontforge.com/en-US/The_EM_Square.html)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification






## LinkML Source

<details>
```yaml
name: BaseLineEnum
description: 'The possible vertical alignments of the text relative to its y-coordinate.

  See the link for an explanation of the meaning of EM square. We do not currently

  support "line-bottom" and "line-top".'
from_schema: https://w3id.org/scverse/vega-scverse/specification
see_also:
- http://designwithfontforge.com/en-US/The_EM_Square.html
rank: 1000
permissible_values:
  top:
    text: top
    description: The highest part of all characters aligns with the y-coordinate.
  middle:
    text: middle
    description: The middle of the fonts EM square aligns with the y-coordinate.
  bottom:
    text: bottom
    description: The bottom of all characters combined aligns with the y-coordinate.
  alphabetic:
    text: alphabetic
    description: "aligns the main body of lowercase letters (like a, e, x) so that\
      \ their base sits exactly on the anchor line \n(y coordinate). Descenders on\
      \ letters like g, p, or y extend below this line."

```
</details>
