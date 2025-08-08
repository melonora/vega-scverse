

# Class: BaselineItem 


_The  vertical alignment of the text relative to its y-coordinate._





URI: [vega_scverse:BaselineItem](https://w3id.org/scverse/vega-scverse/BaselineItem)






```mermaid
 classDiagram
    class BaselineItem
    click BaselineItem href "../BaselineItem"
      BaselineItem : value
        
          
    
        
        
        BaselineItem --> "1" BaseLineEnum : value
        click BaseLineEnum href "../BaseLineEnum"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [BaseLineEnum](BaseLineEnum.md) | The value for the text baseline | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:BaselineItem |
| native | vega_scverse:BaselineItem |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: baselineItem
description: The  vertical alignment of the text relative to its y-coordinate.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: The value for the text baseline.
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
    range: BaseLineEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: baselineItem
description: The  vertical alignment of the text relative to its y-coordinate.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: The value for the text baseline.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    alias: value
    owner: baselineItem
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
    range: BaseLineEnum
    required: true

```
</details>