

# Slot: value 



URI: [vega_scverse:value](https://w3id.org/scverse/vega-scverse/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FontStyleItem](FontStyleItem.md) | Fontstyle of the text |  no  |
| [FontSizeItem](FontSizeItem.md) | Fontsize in pixels of text |  no  |
| [PositionItem](PositionItem.md) | X or y position of an item in pixels |  no  |
| [RGBHexItem](RGBHexItem.md) | RGB value represented by a hexadecimal string value |  no  |
| [BaselineItem](BaselineItem.md) | The  vertical alignment of the text relative to its y-coordinate |  no  |
| [CircleShape](CircleShape.md) | Circle shape definition used in symbol mark |  no  |
| [FontWeightItem](FontWeightItem.md) | Font weight of the text |  no  |
| [FontItem](FontItem.md) | The  name of the font to be used |  no  |
| [TextItem](TextItem.md) | Text to be displayed |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:value |
| native | vega_scverse:value |




## LinkML Source

<details>
```yaml
name: value
alias: value
domain_of:
- PositionItem
- TextItem
- baselineItem
- FontItem
- FontSizeItem
- FontWeightItem
- FontStyleItem
- RGBHexItem
- CircleShape
range: string

```
</details>