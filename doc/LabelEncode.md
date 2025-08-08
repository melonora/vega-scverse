

# Class: LabelEncode 


_A set of visual encoding properties that determine the position and appearance of a 'raster_label' mark. _

_In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data _

_is processed for the first time and a mark instance is newly added to a scene. The update properties are evaluated _

_for all existing (non-exiting) mark instances. The exit properties are evaluated when the data backing a mark is _

_removed, and so the mark is leaving the visual scene. However, in this specification we currently only support_

_enter and update property sets for a 'raster_label' mark._





URI: [vega_scverse:LabelEncode](https://w3id.org/scverse/vega-scverse/LabelEncode)






```mermaid
 classDiagram
    class LabelEncode
    click LabelEncode href "../LabelEncode"
      LabelEncode : enter
        
          
    
        
        
        LabelEncode --> "1" LabelEncodeEnter : enter
        click LabelEncodeEnter href "../LabelEncodeEnter"
    

        
      LabelEncode : update
        
          
    
        
        
        LabelEncode --> "0..1" MarkEncodeUpdate : update
        click MarkEncodeUpdate href "../MarkEncodeUpdate"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [enter](enter.md) | 1 <br/> [LabelEncodeEnter](LabelEncodeEnter.md) | Enter properties that are evaluated when label data is processed for the firs... | direct |
| [update](update.md) | 0..1 <br/> [MarkEncodeUpdate](MarkEncodeUpdate.md) | Update properties that are evaluated for all existing (non-exiting) mark inst... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RasterLabelMark](RasterLabelMark.md) | [encode](encode.md) | range | [LabelEncode](LabelEncode.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:LabelEncode |
| native | vega_scverse:LabelEncode |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabelEncode
description: "A set of visual encoding properties that determine the position and\
  \ appearance of a 'raster_label' mark. \nIn Vega, there are three primary property\
  \ sets: enter, update, exit. The enter properties are evaluated when data \nis processed\
  \ for the first time and a mark instance is newly added to a scene. The update properties\
  \ are evaluated \nfor all existing (non-exiting) mark instances. The exit properties\
  \ are evaluated when the data backing a mark is \nremoved, and so the mark is leaving\
  \ the visual scene. However, in this specification we currently only support\nenter\
  \ and update property sets for a 'raster_label' mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when label data is processed\
      \ for the first time and the raster_label mark \nis newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: LabelEncodeEnter
    required: true
  update:
    name: update
    description: "Update properties that are evaluated for all existing (non-exiting)\
      \ mark instances. Typically included when \nno random coloring is being used\
      \ for the labels."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    domain_of:
    - LabelEncode
    - SymbolEncode
    - PathEncode
    range: MarkEncodeUpdate
    required: false

```
</details>

### Induced

<details>
```yaml
name: LabelEncode
description: "A set of visual encoding properties that determine the position and\
  \ appearance of a 'raster_label' mark. \nIn Vega, there are three primary property\
  \ sets: enter, update, exit. The enter properties are evaluated when data \nis processed\
  \ for the first time and a mark instance is newly added to a scene. The update properties\
  \ are evaluated \nfor all existing (non-exiting) mark instances. The exit properties\
  \ are evaluated when the data backing a mark is \nremoved, and so the mark is leaving\
  \ the visual scene. However, in this specification we currently only support\nenter\
  \ and update property sets for a 'raster_label' mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when label data is processed\
      \ for the first time and the raster_label mark \nis newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    alias: enter
    owner: LabelEncode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: LabelEncodeEnter
    required: true
  update:
    name: update
    description: "Update properties that are evaluated for all existing (non-exiting)\
      \ mark instances. Typically included when \nno random coloring is being used\
      \ for the labels."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    rank: 1000
    alias: update
    owner: LabelEncode
    domain_of:
    - LabelEncode
    - SymbolEncode
    - PathEncode
    range: MarkEncodeUpdate
    required: false

```
</details>