

# Class: ShapesMark 


_Graphical mark for encoding shapes data, using a vega like path mark._





URI: [vega_scverse:ShapesMark](https://w3id.org/scverse/vega-scverse/ShapesMark)






```mermaid
 classDiagram
    class ShapesMark
    click ShapesMark href "../ShapesMark"
      Mark <|-- ShapesMark
        click Mark href "../Mark"
      
      ShapesMark : encode
        
          
    
        
        
        ShapesMark --> "1" PathEncode : encode
        click PathEncode href "../PathEncode"
    

        
      ShapesMark : from_
        
          
    
        
        
        ShapesMark --> "1" MarkDataSource : from_
        click MarkDataSource href "../MarkDataSource"
    

        
      ShapesMark : type
        
          
    
        
        
        ShapesMark --> "1" MarkTypeEnum : type
        click MarkTypeEnum href "../MarkTypeEnum"
    

        
      ShapesMark : zindex
        
      
```





## Inheritance
* [Mark](Mark.md)
    * **ShapesMark**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [MarkTypeEnum](MarkTypeEnum.md) | The type of the mark | [Mark](Mark.md) |
| [from_](from_.md) | 1 <br/> [MarkDataSource](MarkDataSource.md) | The data stream used as the source for the graphical mark | [Mark](Mark.md) |
| [encode](encode.md) | 1 <br/> [PathEncode](PathEncode.md) | A set of visual encoding properties that determine the position and appearanc... | [Mark](Mark.md) |
| [zindex](zindex.md) | 1 <br/> [Integer](Integer.md) | An integer z-index indicating the layering order of sibling mark items | [Mark](Mark.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:ShapesMark |
| native | vega_scverse:ShapesMark |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ShapesMark
description: Graphical mark for encoding shapes data, using a vega like path mark.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
is_a: Mark
slot_usage:
  type:
    name: type
    description: The type of the mark. In this case, it is always 'symbol'.
    ifabsent: string(path)
    equals_string: path
  encode:
    name: encode
    description: A set of visual encoding properties that determine the position and
      appearance of the symbol mark.
    range: PathEncode

```
</details>

### Induced

<details>
```yaml
name: ShapesMark
description: Graphical mark for encoding shapes data, using a vega like path mark.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
is_a: Mark
slot_usage:
  type:
    name: type
    description: The type of the mark. In this case, it is always 'symbol'.
    ifabsent: string(path)
    equals_string: path
  encode:
    name: encode
    description: A set of visual encoding properties that determine the position and
      appearance of the symbol mark.
    range: PathEncode
attributes:
  type:
    name: type
    description: The type of the mark. In this case, it is always 'symbol'.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    ifabsent: string(path)
    alias: type
    owner: ShapesMark
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
    equals_string: path
  from_:
    name: from_
    description: The data stream used as the source for the graphical mark.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    rank: 1000
    alias: from_
    owner: ShapesMark
    domain_of:
    - Mark
    range: MarkDataSource
    required: true
  encode:
    name: encode
    description: A set of visual encoding properties that determine the position and
      appearance of the symbol mark.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    rank: 1000
    alias: encode
    owner: ShapesMark
    domain_of:
    - Mark
    - TextMark
    - GroupMark
    range: PathEncode
    required: true
  zindex:
    name: zindex
    description: "An integer z-index indicating the layering order of sibling mark\
      \ items. The default value is 0. Higher values \n(1) will cause marks to be\
      \ drawn on top of those with lower z-index values."
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    alias: zindex
    owner: ShapesMark
    domain_of:
    - Axis
    - Legend
    - Mark
    - TextMark
    range: integer
    required: true

```
</details>