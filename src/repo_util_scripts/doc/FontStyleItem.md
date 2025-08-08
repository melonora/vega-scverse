

# Class: FontStyleItem 


_Fontstyle of the text._





URI: [vega_scverse:FontStyleItem](https://w3id.org/scverse/vega-scverse/FontStyleItem)






```mermaid
 classDiagram
    class FontStyleItem
    click FontStyleItem href "../FontStyleItem"
      FontStyleItem : value
        
          
    
        
        
        FontStyleItem --> "1" FontStyleEnum : value
        click FontStyleEnum href "../FontStyleEnum"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [FontStyleEnum](FontStyleEnum.md) | The fontstyle value | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TextEncodeEnter](TextEncodeEnter.md) | [fontStyle](fontStyle.md) | range | [FontStyleItem](FontStyleItem.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:FontStyleItem |
| native | vega_scverse:FontStyleItem |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FontStyleItem
description: Fontstyle of the text.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: The fontstyle value.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
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
    range: FontStyleEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: FontStyleItem
description: Fontstyle of the text.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: The fontstyle value.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    alias: value
    owner: FontStyleItem
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
    range: FontStyleEnum
    required: true

```
</details>