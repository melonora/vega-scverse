# Enum: FontWeightEnum 




_Possible font weight values. In case of font weights (100-900), it represents a unitless numeric scale _

_standardized in CSS to represent font weight._



URI: [FontWeightEnum](FontWeightEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| 100 | None | The thinnest font weight available for a given font family |
| 200 | None |  |
| 300 | None |  |
| 400 | None |  |
| 500 | None |  |
| 600 | None |  |
| 700 | None |  |
| 800 | None |  |
| 900 | None | The thickest font weight available for a given font family |
| bold | None | Font with a font weight of 700 |
| normal | None | Font with a font weight of 400 |




## Slots

| Name | Description |
| ---  | --- |
| [labelFontWeight](labelFontWeight.md) | Font weight of axis tick labels |
| [fontWeight](fontWeight.md) | Font weight of the title |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification






## LinkML Source

<details>
```yaml
name: FontWeightEnum
description: "Possible font weight values. In case of font weights (100-900), it represents\
  \ a unitless numeric scale \nstandardized in CSS to represent font weight."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
permissible_values:
  '100':
    text: '100'
    description: The thinnest font weight available for a given font family.
  '200':
    text: '200'
  '300':
    text: '300'
  '400':
    text: '400'
  '500':
    text: '500'
  '600':
    text: '600'
  '700':
    text: '700'
  '800':
    text: '800'
  '900':
    text: '900'
    description: The thickest font weight available for a given font family.
  bold:
    text: bold
    description: Font with a font weight of 700.
  normal:
    text: normal
    description: Font with a font weight of 400.

```
</details>
