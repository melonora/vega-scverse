

# Class: FontSizeItem 


_Fontsize in pixels of text._





URI: [vega_scverse:FontSizeItem](https://w3id.org/scverse/vega-scverse/FontSizeItem)






```mermaid
 classDiagram
    class FontSizeItem
    click FontSizeItem href "../FontSizeItem"
      FontSizeItem : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | Font size value | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TextEncodeEnter](TextEncodeEnter.md) | [fontSize](fontSize.md) | range | [FontSizeItem](FontSizeItem.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:FontSizeItem |
| native | vega_scverse:FontSizeItem |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FontSizeItem
description: Fontsize in pixels of text.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: Font size value.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    slot_uri: nonNegativeFloatSlot
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
    required: true

```
</details>

### Induced

<details>
```yaml
name: FontSizeItem
description: Fontsize in pixels of text.
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  value:
    name: value
    description: Font size value.
    from_schema: https://w3id.org/scverse/vega-scverse/marks
    slot_uri: nonNegativeFloatSlot
    alias: value
    owner: FontSizeItem
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

```
</details>