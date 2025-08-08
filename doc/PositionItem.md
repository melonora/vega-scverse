

# Class: PositionItem 


_X or y position of an item in pixels._





URI: [vega_scverse:PositionItem](https://w3id.org/scverse/vega-scverse/PositionItem)






```mermaid
 classDiagram
    class PositionItem
    click PositionItem href "../PositionItem"
      PositionItem : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Float](Float.md) | The coordinate value | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TextEncodeEnter](TextEncodeEnter.md) | [x](x.md) | range | [PositionItem](PositionItem.md) |
| [TextEncodeEnter](TextEncodeEnter.md) | [y](y.md) | range | [PositionItem](PositionItem.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:PositionItem |
| native | vega_scverse:PositionItem |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PositionItem
description: X or y position of an item in pixels.
from_schema: https://w3id.org/scverse/vega-scverse/specification
attributes:
  value:
    name: value
    description: The coordinate value.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    rank: 1000
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
    range: float
    required: true

```
</details>

### Induced

<details>
```yaml
name: PositionItem
description: X or y position of an item in pixels.
from_schema: https://w3id.org/scverse/vega-scverse/specification
attributes:
  value:
    name: value
    description: The coordinate value.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    rank: 1000
    alias: value
    owner: PositionItem
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
    range: float
    required: true

```
</details>