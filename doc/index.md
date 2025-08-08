# vega-scverse-specification

The configuration entailing all the specification components for visualization of data in the scverse ecosystem.

URI: https://w3id.org/scverse/vega-scverse/specification

Name: vega-scverse-specification



## Classes

| Class | Description |
| --- | --- |
| [Axis](Axis.md) | An axis visualizes a spatial scale mapping for cartesian coordinates using ti... |
| [AxisItem](AxisItem.md) | A axis item which for a mark can define the scale and field used for the axis... |
| [BaselineItem](BaselineItem.md) | The  vertical alignment of the text relative to its y-coordinate |
| [BaseScales](BaseScales.md) | Vega like definition for scales which specifies a collection of mappings from... |
| [CircleShape](CircleShape.md) | Circle shape definition used in symbol mark |
| [ColorItem](ColorItem.md) | A single color item definition specifying the scale on which the color is bas... |
| [ConditionalFillUpdate](ConditionalFillUpdate.md) | Update color based on test condition |
| [ContinuousColorDomain](ContinuousColorDomain.md) | A data domain or source for a LinearColorScale |
| [ContinuousColorMapRange](ContinuousColorMapRange.md) | Color scheme reference for a color palette |
| [DataObject](DataObject.md) | Abstract class for Vega like data set definitions and transforms that define ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpatialDataElementObject](SpatialDataElementObject.md) | Data object pertaining to an element within the SpatialData object |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpatialDataObject](SpatialDataObject.md) | SpatialData object specific to the SpatialData root |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TableObject](TableObject.md) | AnnData Table object stream |
| [FontItem](FontItem.md) | The  name of the font to be used |
| [FontSizeItem](FontSizeItem.md) | Fontsize in pixels of text |
| [FontStyleItem](FontStyleItem.md) | Fontstyle of the text |
| [FontWeightItem](FontWeightItem.md) | Font weight of the text |
| [Format](Format.md) | Format object containing the type of data as object and a string value repres... |
| [GroupEncode](GroupEncode.md) | A set of visual encoding properties that determine the position of a group ma... |
| [GroupEncodeEnter](GroupEncodeEnter.md) | Encoding for the position, width and height of a group mark |
| [GroupMark](GroupMark.md) | Group marks are containers for other marks, and used to create visualizations... |
| [ImageEncode](ImageEncode.md) | A set of visual encoding properties that determine the position and appearanc... |
| [ImageEncodeEnter](ImageEncodeEnter.md) | Enter properties that are evaluated when image data is processed for the firs... |
| [LabelEncode](LabelEncode.md) | A set of visual encoding properties that determine the position and appearanc... |
| [LabelEncodeEnter](LabelEncodeEnter.md) | Enter properties that are evaluated when label data is processed for the firs... |
| [Legend](Legend.md) | Vega like configuration for specifying legends in the SpatialData visualizati... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CategoricalLegend](CategoricalLegend.md) | Type of legend for categorical data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ColorBarLegend](ColorBarLegend.md) | Type of legend for continuous data |
| [Mark](Mark.md) | Graphical marks visually encode data using geometric primitives such as recta... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointsMark](PointsMark.md) | Graphical mark for encoding points data, using a vega like symbol mark |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RasterImageMark](RasterImageMark.md) | Graphical mark encoding an image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RasterLabelMark](RasterLabelMark.md) | Graphical mark encoding a label image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ShapesMark](ShapesMark.md) | Graphical mark for encoding shapes data, using a vega like path mark |
| [MarkDataSource](MarkDataSource.md) | Object with a data field pointing to the name of the datastream that serves a... |
| [MarkEncodeUpdate](MarkEncodeUpdate.md) | Update properties that are evaluated for all existing (non-exiting) mark inst... |
| [Padding](Padding.md) | padding defines the amount of space (in pixels) to reserve between the edge o... |
| [PathEncode](PathEncode.md) | A set of visual encoding properties that determine the position and appearanc... |
| [PathEncodeEnter](PathEncodeEnter.md) | Enter properties that are evaluated when shapes data is processed for the fir... |
| [PointsEncodeEnter](PointsEncodeEnter.md) | Enter properties that are evaluated when points data is processed for the fir... |
| [PositionItem](PositionItem.md) | X or y position of an item in pixels |
| [RandomRGBSignal](RandomRGBSignal.md) | RGB value represented by a hexadecimal string value |
| [RGBHexItem](RGBHexItem.md) | RGB value represented by a hexadecimal string value |
| [Scale](Scale.md) | Base class for vega like scales which map from a data domain to a visual rang... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BaseAxisScale](BaseAxisScale.md) | A vega like scale specifically for mapping from a data domain to an axis rang... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ColorScale](ColorScale.md) | Abstract class to map a data domain to a color range |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BaseCategoricalColorScale](BaseCategoricalColorScale.md) | A scale to map a discrete data domain to discrete colors |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LinearColorScale](LinearColorScale.md) | A vega like scale specifically for mapping from a linear continuous data doma... |
| [SymbolEncode](SymbolEncode.md) | A set of visual encoding properties that determine the position and appearanc... |
| [TextEncode](TextEncode.md) | A set of visual encoding properties that determine the position and appearanc... |
| [TextEncodeEnter](TextEncodeEnter.md) | Enter properties that are evaluated when data for a text mark is processed fo... |
| [TextItem](TextItem.md) | Text to be displayed |
| [TextMark](TextMark.md) | Text marks can be used to annotate data and provide labels and titles for axe... |
| [Title](Title.md) | The title directive adds a descriptive title to a chart |
| [Transform](Transform.md) | Transform of data applied to data input |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AggregateTransform](AggregateTransform.md) | Group and summarize an input data stream to produce a derived output stream u... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FilterChannelTransform](FilterChannelTransform.md) | Filter on particular channels in a raster data object |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FilterTransform](FilterTransform.md) | Select objects from a data stream to keep based on a filter expression |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NormalizationFormulaTransform](NormalizationFormulaTransform.md) | A formula to transform data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpreadTransform](SpreadTransform.md) | Datashade transform expanding each pixel in a rasterized image by a specified... |
| [ViewConfiguration](ViewConfiguration.md) | Viewconfiguration based on vega for the scverse visualization ecosystem |



## Slots

| Slot | Description |
| --- | --- |
| [align](align.md) | The horizontal text alignment relative to the text anchor point |
| [angle](angle.md) | The rotation angle of the text in degrees |
| [as_](as_.md) | The output field names to use for each aggregated field in fields |
| [axes](axes.md) | Axes visualize spatial scale mappings using ticks, grid lines and labels |
| [baseline](baseline.md) | The baseline attribute specifies the vertical alignment (baseline) of the tex... |
| [bottom](bottom.md) | The value for padding at the bottom side of the chart in pixels |
| [color](color.md) | Text color of the title text |
| [columnPadding](columnPadding.md) | The horizontal padding in pixels between symbol legend entries |
| [columns](columns.md) | The number of columns in which to arrange symbol legend entries |
| [count](count.md) | The number of colors to use in the scheme |
| [data](data.md) | Scverse data set definitions and transforms define the data to load and how t... |
| [direction](direction.md) | The direction of the legend, one of 'vertical' or 'horizontal' |
| [domain](domain.md) | The set of input data values that the scale maps from |
| [domainColor](domainColor.md) | Color of axis domain line |
| [domainOpacity](domainOpacity.md) | Opacity of axis domain line |
| [domainWidth](domainWidth.md) | Stroke width of axis domain line |
| [encode](encode.md) | A set of visual encoding properties that determine the position and appearanc... |
| [enter](enter.md) | Enter properties that are evaluated when image data is processed for the firs... |
| [expr](expr.md) | Either the name of the element or coordinate system to filter / select |
| [field](field.md) | The data fields for which to compute aggregate functions |
| [fill](fill.md) | The name of a scale that maps to a fill color |
| [fillColor](fillColor.md) | Hex string representing a RGBA color, which is the background color of the le... |
| [fillOpacity](fillOpacity.md) | Opacity value for the label fill between 0 and 1 |
| [font](font.md) | Font name of the title text |
| [fontSize](fontSize.md) | Font size in pixels of the title text |
| [fontStyle](fontStyle.md) | Fontstyle of the title |
| [fontWeight](fontWeight.md) | Font weight of the title |
| [format](format.md) | Format object containing the type of data as object and a string value repres... |
| [from_](from_.md) | The data stream used as the source for the graphical mark |
| [gradientLength](gradientLength.md) | The length in pixels of the primary axis of a color gradient |
| [gradientOpacity](gradientOpacity.md) | Opacity of the color gradient |
| [gradientStrokeColor](gradientStrokeColor.md) | Stroke color of the color gradient border |
| [gradientStrokeWidth](gradientStrokeWidth.md) | Stroke width of the color gradient border |
| [grid](grid.md) | A boolean flag indicating if grid lines should be included as part of the axi... |
| [gridCap](gridCap.md) | The stroke cap for axis grid lines |
| [gridColor](gridColor.md) | Color of axis grid lines |
| [gridOpacity](gridOpacity.md) | Opacity of axis grid lines |
| [gridWidth](gridWidth.md) | Stroke width of axis grid lines |
| [height](height.md) | The height of the plotting area |
| [labelAlign](labelAlign.md) | Horizontal text alignment for legend labels |
| [labelColor](labelColor.md) | Text color of axis tick labels |
| [labelFont](labelFont.md) | Font name for axis tick labels |
| [labelFontSize](labelFontSize.md) | Font size of axis tick labels |
| [labelFontStyle](labelFontStyle.md) | Font style of axis tick labels |
| [labelFontWeight](labelFontWeight.md) | Font weight of axis tick labels |
| [labelOffset](labelOffset.md) | Offset in pixels between legend labels their corresponding symbol or gradient |
| [labelOpacity](labelOpacity.md) | Opacity of axis tick labels |
| [left](left.md) | The value for padding at the left side of the chart in pixels |
| [legends](legends.md) | Legends visualize scale mappings for visual values such as color, shape and s... |
| [legendX](legendX.md) | The pixel x-coordinate of the legend group |
| [legendY](legendY.md) | The pixel y-coordinate of the legend group |
| [marks](marks.md) | Graphical marks visually encode data using geometric primitives such as recta... |
| [name](name.md) | The name used throughout the view configuration to refer to the data object |
| [nonNegativeFloatSlot](nonNegativeFloatSlot.md) | A positive float value |
| [opacity](opacity.md) | The opacity of the image mark |
| [opacityValueSlot](opacityValueSlot.md) | Opacity value between 0 and 1 |
| [ops](ops.md) | The summary statistic to apply per field |
| [orient](orient.md) | The orientation of the axis, either 'left', 'right', 'top' or 'bottom' |
| [padding](padding.md) | padding defines the amount of space (in pixels) to reserve between the edge o... |
| [px](px.md) | The amount of pixels by which to expand each pixel to make data more visible |
| [range](range.md) | Defines the target visual dimension for the axis scale's output range |
| [rgbaHexSlot](rgbaHexSlot.md) | Hex string representing a RGBA value |
| [rgbHexSlot](rgbHexSlot.md) | Hex string representing a RGB value |
| [right](right.md) | The value for padding at the right side of the chart in pixels |
| [rowPadding](rowPadding.md) | The vertical padding in pixels between symbol legend entries |
| [scale](scale.md) | Name of the 'AxisScale' to visualize as axis object |
| [scales](scales.md) | Scales map data values (numbers, dates, categories, etc |
| [scheme](scheme.md) | The name of the color scheme to use or an array of color values |
| [shape](shape.md) | The type of shape |
| [signal](signal.md) | Signal creating random RGB color for labels in a label raster |
| [size](size.md) | The size of points in a PointsMark |
| [source](source.md) | The source of the SpatialData element |
| [stroke](stroke.md) | The color of the outline of each individual label |
| [strokeColor](strokeColor.md) | Hex string representing a RGBA color, which is the color of the legend border |
| [strokeOpacity](strokeOpacity.md) | Opacity value for the label stroke between 0 and 1 |
| [strokeWidth](strokeWidth.md) | The width of the outline of a labels, symbol or path mark |
| [test](test.md) | The condition to test on, e |
| [text](text.md) | The title text |
| [tickCap](tickCap.md) | The stroke cap for axis tick marks |
| [tickColor](tickColor.md) | Color of axis ticks |
| [tickOpacity](tickOpacity.md) | Opacity of axis ticks |
| [ticks](ticks.md) | A boolean flag indicating if ticks should be included as part of the axis |
| [tickSize](tickSize.md) | The length in pixels of axis ticks |
| [tickWidth](tickWidth.md) | Width in pixels of axis ticks |
| [title](title.md) | The title directive adds a descriptive title to a chart |
| [top](top.md) | The value for padding at the top side of the chart in pixels |
| [transform](transform.md) | An array containing a single transform 'filter_element' with an expression st... |
| [type](type.md) | The type of transform |
| [update](update.md) | Update properties that are evaluated for all existing (non-exiting) mark inst... |
| [url](url.md) | The absolute path to the SpatialData zarr |
| [value](value.md) | The coordinate value |
| [values](values.md) | Explicitly set the visible axis tick and label values |
| [version](version.md) | The version of the data type that is defined |
| [width](width.md) | The width of the plotting area |
| [x](x.md) | The x coordinates |
| [y](y.md) | The y coordinates |
| [zindex](zindex.md) | The integer z-index indicating the layering of the axis group relative to oth... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AggregateOpsEnum](AggregateOpsEnum.md) | The summary statistic to apply for an aggregation transform |
| [AxisEnum](AxisEnum.md) | Possible values for the type of |
| [AxisRangeEnum](AxisRangeEnum.md) | Possible values which to map the data domain to |
| [BaseLineEnum](BaseLineEnum.md) | The possible vertical alignments of the text relative to its y-coordinate |
| [CapEnum](CapEnum.md) | The style of the stroke end for axis tick marks |
| [FontStyleEnum](FontStyleEnum.md) | Possible font styles |
| [FontWeightEnum](FontWeightEnum.md) | Possible font weight values |
| [HorizontalAlignEnum](HorizontalAlignEnum.md) | The horizontal text alignment relative to the anchor point of the text |
| [LegendDirections](LegendDirections.md) | The possible directions of the legend |
| [LegendType](LegendType.md) | The valid mark types within the scverse plotting / visualization ecosystem |
| [MarkTypeEnum](MarkTypeEnum.md) | The valid mark types within the scverse plotting / visualization ecosystem |
| [OrientEnum](OrientEnum.md) | The position relative to the chart for either a (sub)title or axis |
| [ScaleEnum](ScaleEnum.md) | Possible values for the type of Scale |
| [TransformTypeEnum](TransformTypeEnum.md) | Valid transforms on a data stream within a scverse viewconfig |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
