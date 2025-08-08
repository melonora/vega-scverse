

# Class: TextEncode 


_A set of visual encoding properties that determine the position and appearance of a text mark._

_In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data _

_is processed for the first time and a mark instance is newly added to a scene and are the only properties _

_supported for a text mark._





URI: [vega_scverse:TextEncode](https://w3id.org/scverse/vega-scverse/TextEncode)






```mermaid
 classDiagram
    class TextEncode
    click TextEncode href "../TextEncode"
      TextEncode : enter
        
          
    
        
        
        TextEncode --> "1" TextEncodeEnter : enter
        click TextEncodeEnter href "../TextEncodeEnter"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [enter](enter.md) | 1 <br/> [TextEncodeEnter](TextEncodeEnter.md) | Enter properties that are evaluated when data for a text mark is processed fo... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TextMark](TextMark.md) | [encode](encode.md) | range | [TextEncode](TextEncode.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:TextEncode |
| native | vega_scverse:TextEncode |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextEncode
description: "A set of visual encoding properties that determine the position and\
  \ appearance of a text mark.\nIn Vega, there are three primary property sets: enter,\
  \ update, exit. The enter properties are evaluated when data \nis processed for\
  \ the first time and a mark instance is newly added to a scene and are the only\
  \ properties \nsupported for a text mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when data for a text mark is\
      \ processed for the first time and the \ngroup mark is newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: TextEncodeEnter
    required: true

```
</details>

### Induced

<details>
```yaml
name: TextEncode
description: "A set of visual encoding properties that determine the position and\
  \ appearance of a text mark.\nIn Vega, there are three primary property sets: enter,\
  \ update, exit. The enter properties are evaluated when data \nis processed for\
  \ the first time and a mark instance is newly added to a scene and are the only\
  \ properties \nsupported for a text mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when data for a text mark is\
      \ processed for the first time and the \ngroup mark is newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    alias: enter
    owner: TextEncode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: TextEncodeEnter
    required: true

```
</details>