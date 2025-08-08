

# Class: TextItem 


_Text to be displayed. Value is an array where each element corresponds to 1 line._





URI: [vega_scverse:TextItem](https://w3id.org/scverse/vega-scverse/TextItem)






```mermaid
 classDiagram
    class TextItem
    click TextItem href "../TextItem"
      TextItem : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [String](String.md) | The value for text | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TextEncodeEnter](TextEncodeEnter.md) | [text](text.md) | range | [TextItem](TextItem.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:TextItem |
| native | vega_scverse:TextItem |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextItem
description: Text to be displayed. Value is an array where each element corresponds
  to 1 line.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: The value for text.
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
    range: string
    required: true
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: TextItem
description: Text to be displayed. Value is an array where each element corresponds
  to 1 line.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: The value for text.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    alias: value
    owner: TextItem
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
    required: true
    multivalued: true

```
</details>