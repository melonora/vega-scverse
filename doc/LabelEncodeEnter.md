

# Class: LabelEncodeEnter 


_Enter properties that are evaluated when label data is processed for the first time and the raster_image mark is _

_newly added to a scene._





URI: [vega_scverse:LabelEncodeEnter](https://w3id.org/scverse/vega-scverse/LabelEncodeEnter)






```mermaid
 classDiagram
    class LabelEncodeEnter
    click LabelEncodeEnter href "../LabelEncodeEnter"
      LabelEncodeEnter : fill
        
      LabelEncodeEnter : fillOpacity
        
      LabelEncodeEnter : stroke
        
          
    
        
        
        LabelEncodeEnter --> "1" ColorItem : stroke
        click ColorItem href "../ColorItem"
    

        
      LabelEncodeEnter : strokeOpacity
        
      LabelEncodeEnter : strokeWidth
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [stroke](stroke.md) | 1 <br/> [ColorItem](ColorItem.md) | The color of the outline of each individual label | direct |
| [fill](fill.md) | 1 <br/> [String](String.md)&nbsp;or&nbsp;<br />[ColorItem](ColorItem.md)&nbsp;or&nbsp;<br />[RandomRGBSignal](RandomRGBSignal.md) | The color fill of each individual label | direct |
| [fillOpacity](fillOpacity.md) | 1 <br/> [String](String.md) | Opacity value for the label fill between 0 and 1 | direct |
| [strokeOpacity](strokeOpacity.md) | 1 <br/> [String](String.md) | Opacity value for the label stroke between 0 and 1 | direct |
| [strokeWidth](strokeWidth.md) | 1 <br/> [String](String.md) | The width of the label outlines in pixels | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [LabelEncode](LabelEncode.md) | [enter](enter.md) | range | [LabelEncodeEnter](LabelEncodeEnter.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:LabelEncodeEnter |
| native | vega_scverse:LabelEncodeEnter |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabelEncodeEnter
description: "Enter properties that are evaluated when label data is processed for\
  \ the first time and the raster_image mark is \nnewly added to a scene."
from_schema: https://w3id.org/scverse/vega-scverse/specification
attributes:
  stroke:
    name: stroke
    description: The color of the outline of each individual label.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    domain_of:
    - LabelEncodeEnter
    - PointsEncodeEnter
    range: ColorItem
    required: true
    multivalued: true
    exact_cardinality: 1
  fill:
    name: fill
    description: The color fill of each individual label.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    domain_of:
    - Legend
    - ImageEncodeEnter
    - LabelEncodeEnter
    - PointsEncodeEnter
    - PathEncodeEnter
    - TextEncodeEnter
    - MarkEncodeUpdate
    required: true
    multivalued: true
    exact_cardinality: 1
    any_of:
    - range: ColorItem
    - range: RandomRGBSignal
  fillOpacity:
    name: fillOpacity
    description: Opacity value for the label fill between 0 and 1.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    slot_uri: opacityValueSlot
    domain_of:
    - LabelEncodeEnter
    - PointsEncodeEnter
    - PathEncodeEnter
    - TextEncodeEnter
    required: true
  strokeOpacity:
    name: strokeOpacity
    description: Opacity value for the label stroke between 0 and 1.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    slot_uri: opacityValueSlot
    domain_of:
    - LabelEncodeEnter
    - PointsEncodeEnter
    required: true
  strokeWidth:
    name: strokeWidth
    description: The width of the label outlines in pixels.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    slot_uri: strokeWidth
    domain_of:
    - Legend
    - LabelEncodeEnter
    - PointsEncodeEnter
    required: true

```
</details>

### Induced

<details>
```yaml
name: LabelEncodeEnter
description: "Enter properties that are evaluated when label data is processed for\
  \ the first time and the raster_image mark is \nnewly added to a scene."
from_schema: https://w3id.org/scverse/vega-scverse/specification
attributes:
  stroke:
    name: stroke
    description: The color of the outline of each individual label.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    alias: stroke
    owner: LabelEncodeEnter
    domain_of:
    - LabelEncodeEnter
    - PointsEncodeEnter
    range: ColorItem
    required: true
    multivalued: true
    exact_cardinality: 1
  fill:
    name: fill
    description: The color fill of each individual label.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    alias: fill
    owner: LabelEncodeEnter
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
    multivalued: true
    exact_cardinality: 1
    any_of:
    - range: ColorItem
    - range: RandomRGBSignal
  fillOpacity:
    name: fillOpacity
    description: Opacity value for the label fill between 0 and 1.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    slot_uri: opacityValueSlot
    alias: fillOpacity
    owner: LabelEncodeEnter
    domain_of:
    - LabelEncodeEnter
    - PointsEncodeEnter
    - PathEncodeEnter
    - TextEncodeEnter
    range: string
    required: true
  strokeOpacity:
    name: strokeOpacity
    description: Opacity value for the label stroke between 0 and 1.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    slot_uri: opacityValueSlot
    alias: strokeOpacity
    owner: LabelEncodeEnter
    domain_of:
    - LabelEncodeEnter
    - PointsEncodeEnter
    range: string
    required: true
  strokeWidth:
    name: strokeWidth
    description: The width of the label outlines in pixels.
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    slot_uri: strokeWidth
    alias: strokeWidth
    owner: LabelEncodeEnter
    domain_of:
    - Legend
    - LabelEncodeEnter
    - PointsEncodeEnter
    range: string
    required: true

```
</details>