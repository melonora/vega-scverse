# Enum: FontStyleEnum 




_Possible font styles. These are all the possible css font styles. These include styles,_

_weights, variants and stretch. In case of font weights (100-900), it represents a unitless numeric scale _

_standardized in CSS to represent font weight._



URI: [FontStyleEnum](FontStyleEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| normal | None | Regular CSS font style with a font weight of 400 |
| italic | None | A cursive CSS font style |
| bold | None | A font with a thicker stroke weight relative to a regular font used to emphas... |
| 100 | None | The thinnest font weight available for a given font family |
| 200 | None |  |
| 300 | None |  |
| 500 | None |  |
| 600 | None |  |
| 800 | None |  |
| 900 | None | The thickest font weight available for a given font family |
| small-caps | None | Uppercase letterforms designed at approximately the same height and weight as... |
| ultra-condensed | None | The most horizontally narrow font stretch |
| extra-condensed | None |  |
| condensed | None |  |
| semi-condensed | None |  |
| semi-expanded | None |  |
| expanded | None |  |
| extra-expanded | None |  |
| ultra-expanded | None | The most horizontally expanded font stretch |




## Slots

| Name | Description |
| ---  | --- |
| [labelFontStyle](labelFontStyle.md) | Font style of axis tick labels |
| [fontStyle](fontStyle.md) | Fontstyle of the title |






## See Also

* [https://www.w3.org/Style/Examples/007/fonts.en.html#font-style](https://www.w3.org/Style/Examples/007/fonts.en.html#font-style)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification






## LinkML Source

<details>
```yaml
name: FontStyleEnum
description: "Possible font styles. These are all the possible css font styles. These\
  \ include styles,\nweights, variants and stretch. In case of font weights (100-900),\
  \ it represents a unitless numeric scale \nstandardized in CSS to represent font\
  \ weight."
from_schema: https://w3id.org/scverse/vega-scverse/specification
see_also:
- https://www.w3.org/Style/Examples/007/fonts.en.html#font-style
rank: 1000
permissible_values:
  normal:
    text: normal
    description: Regular CSS font style with a font weight of 400.
  italic:
    text: italic
    description: A cursive CSS font style.
  bold:
    text: bold
    description: 'A font with a thicker stroke weight relative to a regular font used
      to emphasize the text. It has a font weight

      of 700.'
  '100':
    text: '100'
    description: The thinnest font weight available for a given font family.
  '200':
    text: '200'
  '300':
    text: '300'
  '500':
    text: '500'
  '600':
    text: '600'
  '800':
    text: '800'
  '900':
    text: '900'
    description: The thickest font weight available for a given font family.
  small-caps:
    text: small-caps
    description: Uppercase letterforms designed at approximately the same height and
      weight as the font's lowercase letters.
  ultra-condensed:
    text: ultra-condensed
    description: 'The most horizontally narrow font stretch. The visual representation
      of each character is narrowed to its most

      compressed form.'
  extra-condensed:
    text: extra-condensed
  condensed:
    text: condensed
  semi-condensed:
    text: semi-condensed
  semi-expanded:
    text: semi-expanded
  expanded:
    text: expanded
  extra-expanded:
    text: extra-expanded
  ultra-expanded:
    text: ultra-expanded
    description: 'The most horizontally expanded font stretch. The visual representation
      of each character is expanded to its most

      expanded form.'

```
</details>
