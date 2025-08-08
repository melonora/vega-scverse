

# Slot: encode 



URI: [vega_scverse:encode](https://w3id.org/scverse/vega-scverse/encode)
Alias: encode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RasterImageMark](RasterImageMark.md) | Graphical mark encoding an image |  yes  |
| [GroupMark](GroupMark.md) | Group marks are containers for other marks, and used to create visualizations... |  no  |
| [Mark](Mark.md) | Graphical marks visually encode data using geometric primitives such as recta... |  no  |
| [PointsMark](PointsMark.md) | Graphical mark for encoding points data, using a vega like symbol mark |  yes  |
| [TextMark](TextMark.md) | Text marks can be used to annotate data and provide labels and titles for axe... |  no  |
| [ShapesMark](ShapesMark.md) | Graphical mark for encoding shapes data, using a vega like path mark |  yes  |
| [RasterLabelMark](RasterLabelMark.md) | Graphical mark encoding a label image |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:encode |
| native | vega_scverse:encode |




## LinkML Source

<details>
```yaml
name: encode
alias: encode
domain_of:
- Mark
- TextMark
- GroupMark
range: string

```
</details>