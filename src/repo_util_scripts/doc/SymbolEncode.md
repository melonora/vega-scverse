

# Class: SymbolEncode 


_A set of visual encoding properties that determine the position and appearance of a 'symbol' mark. _

_In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data _

_is processed for the first time and a mark instance is newly added to a scene. The update properties are evaluated _

_for all existing (non-exiting) mark instances. The exit properties are evaluated when the data backing a mark is _

_removed, and so the mark is leaving the visual scene. However, in this specification we currently only support_

_enter and update property sets for a 'symbol' mark._





URI: [vega_scverse:SymbolEncode](https://w3id.org/scverse/vega-scverse/SymbolEncode)






```mermaid
 classDiagram
    class SymbolEncode
    click SymbolEncode href "../SymbolEncode"
      SymbolEncode : enter
        
          
    
        
        
        SymbolEncode --> "1" PointsEncodeEnter : enter
        click PointsEncodeEnter href "../PointsEncodeEnter"
    

        
      SymbolEncode : update
        
          
    
        
        
        SymbolEncode --> "0..1" MarkEncodeUpdate : update
        click MarkEncodeUpdate href "../MarkEncodeUpdate"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [enter](enter.md) | 1 <br/> [PointsEncodeEnter](PointsEncodeEnter.md) | Enter properties that are evaluated when points data is processed for the fir... | direct |
| [update](update.md) | 0..1 <br/> [MarkEncodeUpdate](MarkEncodeUpdate.md) | Update properties that are evaluated for all existing (non-exiting) mark inst... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PointsMark](PointsMark.md) | [encode](encode.md) | range | [SymbolEncode](SymbolEncode.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:SymbolEncode |
| native | vega_scverse:SymbolEncode |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SymbolEncode
description: "A set of visual encoding properties that determine the position and\
  \ appearance of a 'symbol' mark. \nIn Vega, there are three primary property sets:\
  \ enter, update, exit. The enter properties are evaluated when data \nis processed\
  \ for the first time and a mark instance is newly added to a scene. The update properties\
  \ are evaluated \nfor all existing (non-exiting) mark instances. The exit properties\
  \ are evaluated when the data backing a mark is \nremoved, and so the mark is leaving\
  \ the visual scene. However, in this specification we currently only support\nenter\
  \ and update property sets for a 'symbol' mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when points data is processed\
      \ for the first time and the points mark \nis newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: PointsEncodeEnter
    required: true
  update:
    name: update
    description: "Update properties that are evaluated for all existing (non-exiting)\
      \ mark instances. Usually defined if the \nuser specified a color to be used\
      \ for the PointsMark."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
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
name: SymbolEncode
description: "A set of visual encoding properties that determine the position and\
  \ appearance of a 'symbol' mark. \nIn Vega, there are three primary property sets:\
  \ enter, update, exit. The enter properties are evaluated when data \nis processed\
  \ for the first time and a mark instance is newly added to a scene. The update properties\
  \ are evaluated \nfor all existing (non-exiting) mark instances. The exit properties\
  \ are evaluated when the data backing a mark is \nremoved, and so the mark is leaving\
  \ the visual scene. However, in this specification we currently only support\nenter\
  \ and update property sets for a 'symbol' mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when points data is processed\
      \ for the first time and the points mark \nis newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    alias: enter
    owner: SymbolEncode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: PointsEncodeEnter
    required: true
  update:
    name: update
    description: "Update properties that are evaluated for all existing (non-exiting)\
      \ mark instances. Usually defined if the \nuser specified a color to be used\
      \ for the PointsMark."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    alias: update
    owner: SymbolEncode
    domain_of:
    - LabelEncode
    - SymbolEncode
    - PathEncode
    range: MarkEncodeUpdate
    required: false

```
</details>