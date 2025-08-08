

# Class: RasterLabelMark 


_Graphical mark encoding a label image._





URI: [vega_scverse:RasterLabelMark](https://w3id.org/scverse/vega-scverse/RasterLabelMark)






```mermaid
 classDiagram
    class RasterLabelMark
    click RasterLabelMark href "../RasterLabelMark"
      Mark <|-- RasterLabelMark
        click Mark href "../Mark"
      
      RasterLabelMark : encode
        
          
    
        
        
        RasterLabelMark --> "1" LabelEncode : encode
        click LabelEncode href "../LabelEncode"
    

        
      RasterLabelMark : from_
        
          
    
        
        
        RasterLabelMark --> "1" MarkDataSource : from_
        click MarkDataSource href "../MarkDataSource"
    

        
      RasterLabelMark : type
        
          
    
        
        
        RasterLabelMark --> "1" MarkTypeEnum : type
        click MarkTypeEnum href "../MarkTypeEnum"
    

        
      RasterLabelMark : zindex
        
      
```





## Inheritance
* [Mark](Mark.md)
    * **RasterLabelMark**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [MarkTypeEnum](MarkTypeEnum.md) | The type of the mark | [Mark](Mark.md) |
| [from_](from_.md) | 1 <br/> [MarkDataSource](MarkDataSource.md) | The data stream used as the source for the graphical mark | [Mark](Mark.md) |
| [encode](encode.md) | 1 <br/> [LabelEncode](LabelEncode.md) | A set of visual encoding properties that determine the position and appearanc... | [Mark](Mark.md) |
| [zindex](zindex.md) | 1 <br/> [Integer](Integer.md) | An integer z-index indicating the layering order of sibling mark items | [Mark](Mark.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:RasterLabelMark |
| native | vega_scverse:RasterLabelMark |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RasterLabelMark
description: Graphical mark encoding a label image.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
is_a: Mark
slot_usage:
  type:
    name: type
    description: The type of the mark. In this case, it is always 'raster_label'
    ifabsent: string(raster_label)
    equals_string: raster_label
  encode:
    name: encode
    description: A set of visual encoding properties that determine the position and
      appearance of the raster_image mark.
    range: LabelEncode

```
</details>

### Induced

<details>
```yaml
name: RasterLabelMark
description: Graphical mark encoding a label image.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
is_a: Mark
slot_usage:
  type:
    name: type
    description: The type of the mark. In this case, it is always 'raster_label'
    ifabsent: string(raster_label)
    equals_string: raster_label
  encode:
    name: encode
    description: A set of visual encoding properties that determine the position and
      appearance of the raster_image mark.
    range: LabelEncode
attributes:
  type:
    name: type
    description: The type of the mark. In this case, it is always 'raster_label'
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    ifabsent: string(raster_label)
    alias: type
    owner: RasterLabelMark
    domain_of:
    - Transform
    - Format
    - Scale
    - Legend
    - Mark
    - TextMark
    - GroupMark
    range: MarkTypeEnum
    required: true
    equals_string: raster_label
  from_:
    name: from_
    description: The data stream used as the source for the graphical mark.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    rank: 1000
    alias: from_
    owner: RasterLabelMark
    domain_of:
    - Mark
    range: MarkDataSource
    required: true
  encode:
    name: encode
    description: A set of visual encoding properties that determine the position and
      appearance of the raster_image mark.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    rank: 1000
    alias: encode
    owner: RasterLabelMark
    domain_of:
    - Mark
    - TextMark
    - GroupMark
    range: LabelEncode
    required: true
  zindex:
    name: zindex
    description: "An integer z-index indicating the layering order of sibling mark\
      \ items. The default value is 0. Higher values \n(1) will cause marks to be\
      \ drawn on top of those with lower z-index values."
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    alias: zindex
    owner: RasterLabelMark
    domain_of:
    - Axis
    - Legend
    - Mark
    - TextMark
    range: integer
    required: true

```
</details>