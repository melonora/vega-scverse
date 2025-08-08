

# Class: ColorBarLegend 


_Type of legend for continuous data._





URI: [vega_scverse:ColorBarLegend](https://w3id.org/scverse/vega-scverse/ColorBarLegend)






```mermaid
 classDiagram
    class ColorBarLegend
    click ColorBarLegend href "../ColorBarLegend"
      Legend <|-- ColorBarLegend
        click Legend href "../Legend"
      
      ColorBarLegend : direction
        
          
    
        
        
        ColorBarLegend --> "1" LegendDirections : direction
        click LegendDirections href "../LegendDirections"
    

        
      ColorBarLegend : fill
        
      ColorBarLegend : fillColor
        
      ColorBarLegend : gradientLength
        
      ColorBarLegend : gradientOpacity
        
      ColorBarLegend : gradientStrokeColor
        
      ColorBarLegend : gradientStrokeWidth
        
      ColorBarLegend : labelAlign
        
          
    
        
        
        ColorBarLegend --> "1" HorizontalAlignEnum : labelAlign
        click HorizontalAlignEnum href "../HorizontalAlignEnum"
    

        
      ColorBarLegend : labelColor
        
      ColorBarLegend : labelFont
        
      ColorBarLegend : labelFontSize
        
      ColorBarLegend : labelFontStyle
        
          
    
        
        
        ColorBarLegend --> "1" FontStyleEnum : labelFontStyle
        click FontStyleEnum href "../FontStyleEnum"
    

        
      ColorBarLegend : labelFontWeight
        
          
    
        
        
        ColorBarLegend --> "1" FontWeightEnum : labelFontWeight
        click FontWeightEnum href "../FontWeightEnum"
    

        
      ColorBarLegend : labelOffset
        
      ColorBarLegend : labelOpacity
        
      ColorBarLegend : legendX
        
      ColorBarLegend : legendY
        
      ColorBarLegend : orient
        
      ColorBarLegend : padding
        
      ColorBarLegend : strokeColor
        
      ColorBarLegend : strokeWidth
        
      ColorBarLegend : type
        
          
    
        
        
        ColorBarLegend --> "1" LegendType : type
        click LegendType href "../LegendType"
    

        
      ColorBarLegend : zindex
        
      
```





## Inheritance
* [Legend](Legend.md)
    * **ColorBarLegend**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [gradientLength](gradientLength.md) | 1 <br/> [Float](Float.md) | The length in pixels of the primary axis of a color gradient | direct |
| [gradientOpacity](gradientOpacity.md) | 1 <br/> [String](String.md) | Opacity of the color gradient | direct |
| [gradientStrokeColor](gradientStrokeColor.md) | 1 <br/> [String](String.md) | Stroke color of the color gradient border | direct |
| [gradientStrokeWidth](gradientStrokeWidth.md) | 1 <br/> [Float](Float.md) | Stroke width of the color gradient border | direct |
| [type](type.md) | 1 <br/> [LegendType](LegendType.md) | The type of legend, either 'gradient' (continuous data) or 'discrete' (catego... | [Legend](Legend.md) |
| [direction](direction.md) | 1 <br/> [LegendDirections](LegendDirections.md) | The direction of the legend, one of 'vertical' or 'horizontal' | [Legend](Legend.md) |
| [orient](orient.md) | 0..1 <br/> [String](String.md) | The orientation of the legend, determining where the legend is placed relativ... | [Legend](Legend.md) |
| [padding](padding.md) | 0..1 <br/> [Float](Float.md) | The padding between the border and content of the legend group in pixels | [Legend](Legend.md) |
| [fill](fill.md) | 1 <br/> [String](String.md) | The name of a scale that maps to a fill color | [Legend](Legend.md) |
| [fillColor](fillColor.md) | 0..1 <br/> [String](String.md) | Hex string representing a RGBA color, which is the background color of the le... | [Legend](Legend.md) |
| [strokeColor](strokeColor.md) | 0..1 <br/> [String](String.md) | Hex string representing a RGBA color, which is the color of the legend border | [Legend](Legend.md) |
| [strokeWidth](strokeWidth.md) | 0..1 <br/> [Float](Float.md) | The width of the legend border in pixels | [Legend](Legend.md) |
| [labelOffset](labelOffset.md) | 1 <br/> [Float](Float.md) | Offset in pixels between legend labels their corresponding symbol or gradient | [Legend](Legend.md) |
| [labelAlign](labelAlign.md) | 1 <br/> [HorizontalAlignEnum](HorizontalAlignEnum.md) | Horizontal text alignment for legend labels | [Legend](Legend.md) |
| [labelColor](labelColor.md) | 1 <br/> [String](String.md) | Text color for legend labels represented by a RGB hex string | [Legend](Legend.md) |
| [labelOpacity](labelOpacity.md) | 1 <br/> [String](String.md) | The opacity of legend labels | [Legend](Legend.md) |
| [labelFont](labelFont.md) | 0..1 <br/> [String](String.md) | Font name for legend labels | [Legend](Legend.md) |
| [labelFontSize](labelFontSize.md) | 1 <br/> [Float](Float.md) | Font size in pixels for legend labels | [Legend](Legend.md) |
| [labelFontStyle](labelFontStyle.md) | 1 <br/> [FontStyleEnum](FontStyleEnum.md) | Font style of legend labels | [Legend](Legend.md) |
| [labelFontWeight](labelFontWeight.md) | 1 <br/> [FontWeightEnum](FontWeightEnum.md) | Font weight of legend labels | [Legend](Legend.md) |
| [legendX](legendX.md) | 1 <br/> [Float](Float.md) | The pixel x-coordinate of the legend group | [Legend](Legend.md) |
| [legendY](legendY.md) | 1 <br/> [Float](Float.md) | The pixel y-coordinate of the legend group | [Legend](Legend.md) |
| [zindex](zindex.md) | 1 <br/> [Float](Float.md) | The integer z-index indicating the layering of the legend group relative to o... | [Legend](Legend.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:ColorBarLegend |
| native | vega_scverse:ColorBarLegend |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ColorBarLegend
description: Type of legend for continuous data.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
is_a: Legend
attributes:
  gradientLength:
    name: gradientLength
    description: "The length in pixels of the primary axis of a color gradient. This\
      \ value corresponds to the height of a \nvertical gradient or the width of a\
      \ horizontal gradient."
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    domain_of:
    - ColorBarLegend
    range: float
    required: true
  gradientOpacity:
    name: gradientOpacity
    description: Opacity of the color gradient.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    slot_uri: opacityValueSlot
    domain_of:
    - ColorBarLegend
    required: true
  gradientStrokeColor:
    name: gradientStrokeColor
    description: Stroke color of the color gradient border.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    slot_uri: rgbHexSlot
    domain_of:
    - ColorBarLegend
    required: true
  gradientStrokeWidth:
    name: gradientStrokeWidth
    description: Stroke width of the color gradient border.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    domain_of:
    - ColorBarLegend
    range: float
    required: true

```
</details>

### Induced

<details>
```yaml
name: ColorBarLegend
description: Type of legend for continuous data.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
is_a: Legend
attributes:
  gradientLength:
    name: gradientLength
    description: "The length in pixels of the primary axis of a color gradient. This\
      \ value corresponds to the height of a \nvertical gradient or the width of a\
      \ horizontal gradient."
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: gradientLength
    owner: ColorBarLegend
    domain_of:
    - ColorBarLegend
    range: float
    required: true
  gradientOpacity:
    name: gradientOpacity
    description: Opacity of the color gradient.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    slot_uri: opacityValueSlot
    alias: gradientOpacity
    owner: ColorBarLegend
    domain_of:
    - ColorBarLegend
    range: string
    required: true
  gradientStrokeColor:
    name: gradientStrokeColor
    description: Stroke color of the color gradient border.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    slot_uri: rgbHexSlot
    alias: gradientStrokeColor
    owner: ColorBarLegend
    domain_of:
    - ColorBarLegend
    range: string
    required: true
  gradientStrokeWidth:
    name: gradientStrokeWidth
    description: Stroke width of the color gradient border.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: gradientStrokeWidth
    owner: ColorBarLegend
    domain_of:
    - ColorBarLegend
    range: float
    required: true
  type:
    name: type
    description: The type of legend, either 'gradient' (continuous data) or 'discrete'
      (categorical data).
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: type
    owner: ColorBarLegend
    domain_of:
    - Transform
    - Format
    - Scale
    - Legend
    - Mark
    - TextMark
    - GroupMark
    range: legendType
    required: true
  direction:
    name: direction
    description: The direction of the legend, one of 'vertical' or 'horizontal'.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: direction
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: legendDirections
    required: true
  orient:
    name: orient
    description: "The orientation of the legend, determining where the legend is placed\
      \ relative to a chart's data rectangle. \nCurrently, only 'none' is allowed\
      \ here as in Vega this allows to directly specify the positioning in \npixel\
      \ coordinates. If there is demand, this can be changed."
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    ifabsent: string(none)
    alias: orient
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    - Title
    range: string
    equals_string: none
  padding:
    name: padding
    description: The padding between the border and content of the legend group in
      pixels.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: padding
    owner: ColorBarLegend
    domain_of:
    - ViewConfiguration
    - Legend
    range: float
  fill:
    name: fill
    description: 'The name of a scale that maps to a fill color. This represents the
      color used to visualize discrete classes

      or continuous data in the legend.'
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: fill
    owner: ColorBarLegend
    domain_of:
    - Legend
    - ImageEncodeEnter
    - LabelEncodeEnter
    - PointsEncodeEnter
    - PathEncodeEnter
    - TextEncodeEnter
    - MarkEncodeUpdate
    range: string
    required: true
    pattern: ^color_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
  fillColor:
    name: fillColor
    description: Hex string representing a RGBA color, which is the background color
      of the legend.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    slot_uri: rgbaHexSlot
    alias: fillColor
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: string
  strokeColor:
    name: strokeColor
    description: Hex string representing a RGBA color, which is the color of the legend
      border.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    slot_uri: rgbaHexSlot
    alias: strokeColor
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: string
  strokeWidth:
    name: strokeWidth
    description: "The width of the legend border in pixels. This property deviates\
      \ from its Vega equivalent, in that the \nvega equivalent expects a 'Scale'."
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: strokeWidth
    owner: ColorBarLegend
    domain_of:
    - Legend
    - LabelEncodeEnter
    - PointsEncodeEnter
    range: float
  labelOffset:
    name: labelOffset
    description: Offset in pixels between legend labels their corresponding symbol
      or gradient.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: labelOffset
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: float
    required: true
  labelAlign:
    name: labelAlign
    description: 'Horizontal text alignment for legend labels. In short this means
      where the label text is relative to the

      anchor point of the labels (this could be defined as the coordinates where the
      labels are specified to be).'
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: labelAlign
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: HorizontalAlignEnum
    required: true
  labelColor:
    name: labelColor
    description: Text color for legend labels represented by a RGB hex string.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    slot_uri: rgbHexSlot
    alias: labelColor
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    range: string
    required: true
  labelOpacity:
    name: labelOpacity
    description: The opacity of legend labels.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    slot_uri: opacityValueSlot
    alias: labelOpacity
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    range: string
    required: true
  labelFont:
    name: labelFont
    description: Font name for legend labels.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    ifabsent: string(Arial)
    alias: labelFont
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    range: string
  labelFontSize:
    name: labelFontSize
    description: Font size in pixels for legend labels.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: labelFontSize
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    range: float
    required: true
  labelFontStyle:
    name: labelFontStyle
    description: Font style of legend labels
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: labelFontStyle
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    range: FontStyleEnum
    required: true
  labelFontWeight:
    name: labelFontWeight
    description: Font weight of legend labels.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: labelFontWeight
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    range: FontWeightEnum
    required: true
  legendX:
    name: legendX
    description: The pixel x-coordinate of the legend group.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: legendX
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: float
    required: true
  legendY:
    name: legendY
    description: The pixel y-coordinate of the legend group.
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    rank: 1000
    alias: legendY
    owner: ColorBarLegend
    domain_of:
    - Legend
    range: float
    required: true
  zindex:
    name: zindex
    description: "The integer z-index indicating the layering of the legend group\
      \ relative to other axis, mark, and \nlegend groups."
    from_schema: https://w3id.org/scverse/vega-scverse/legends
    alias: zindex
    owner: ColorBarLegend
    domain_of:
    - Axis
    - Legend
    - Mark
    - TextMark
    range: float
    required: true

```
</details>