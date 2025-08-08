

# Slot: type 



URI: [vega_scverse:type](https://w3id.org/scverse/vega-scverse/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transform](Transform.md) | Transform of data applied to data input |  no  |
| [CategoricalLegend](CategoricalLegend.md) | Type of legend for categorical data |  no  |
| [Mark](Mark.md) | Graphical marks visually encode data using geometric primitives such as recta... |  no  |
| [FilterChannelTransform](FilterChannelTransform.md) | Filter on particular channels in a raster data object |  yes  |
| [ShapesMark](ShapesMark.md) | Graphical mark for encoding shapes data, using a vega like path mark |  yes  |
| [Format](Format.md) | Format object containing the type of data as object and a string value repres... |  no  |
| [RasterImageMark](RasterImageMark.md) | Graphical mark encoding an image |  yes  |
| [GroupMark](GroupMark.md) | Group marks are containers for other marks, and used to create visualizations... |  no  |
| [Legend](Legend.md) | Vega like configuration for specifying legends in the SpatialData visualizati... |  no  |
| [ColorBarLegend](ColorBarLegend.md) | Type of legend for continuous data |  no  |
| [PointsMark](PointsMark.md) | Graphical mark for encoding points data, using a vega like symbol mark |  yes  |
| [BaseAxisScale](BaseAxisScale.md) | A vega like scale specifically for mapping from a data domain to an axis rang... |  yes  |
| [RasterLabelMark](RasterLabelMark.md) | Graphical mark encoding a label image |  yes  |
| [ColorScale](ColorScale.md) | Abstract class to map a data domain to a color range |  no  |
| [AggregateTransform](AggregateTransform.md) | Group and summarize an input data stream to produce a derived output stream u... |  yes  |
| [FilterTransform](FilterTransform.md) | Select objects from a data stream to keep based on a filter expression |  yes  |
| [NormalizationFormulaTransform](NormalizationFormulaTransform.md) | A formula to transform data |  yes  |
| [Scale](Scale.md) | Base class for vega like scales which map from a data domain to a visual rang... |  no  |
| [SpreadTransform](SpreadTransform.md) | Datashade transform expanding each pixel in a rasterized image by a specified... |  yes  |
| [LinearColorScale](LinearColorScale.md) | A vega like scale specifically for mapping from a linear continuous data doma... |  yes  |
| [TextMark](TextMark.md) | Text marks can be used to annotate data and provide labels and titles for axe... |  no  |
| [BaseCategoricalColorScale](BaseCategoricalColorScale.md) | A scale to map a discrete data domain to discrete colors |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:type |
| native | vega_scverse:type |




## LinkML Source

<details>
```yaml
name: type
alias: type
domain_of:
- Transform
- Format
- Scale
- Legend
- Mark
- TextMark
- GroupMark
range: string

```
</details>