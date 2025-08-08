

# Class: GroupEncode 


_A set of visual encoding properties that determine the position of a group mark, which are used for subplots. _

_In Vega, there are three primary property sets: enter, update, exit. The enter properties are evaluated when data _

_is processed for the first time and a mark instance is newly added to a scene and are the only properties _

_supported for a group mark._





URI: [vega_scverse:GroupEncode](https://w3id.org/scverse/vega-scverse/GroupEncode)






```mermaid
 classDiagram
    class GroupEncode
    click GroupEncode href "../GroupEncode"
      GroupEncode : enter
        
          
    
        
        
        GroupEncode --> "1" GroupEncodeEnter : enter
        click GroupEncodeEnter href "../GroupEncodeEnter"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [enter](enter.md) | 1 <br/> [GroupEncodeEnter](GroupEncodeEnter.md) | Enter properties that are evaluated when data for a group mark is processed f... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GroupMark](GroupMark.md) | [encode](encode.md) | range | [GroupEncode](GroupEncode.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:GroupEncode |
| native | vega_scverse:GroupEncode |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GroupEncode
description: "A set of visual encoding properties that determine the position of a\
  \ group mark, which are used for subplots. \nIn Vega, there are three primary property\
  \ sets: enter, update, exit. The enter properties are evaluated when data \nis processed\
  \ for the first time and a mark instance is newly added to a scene and are the only\
  \ properties \nsupported for a group mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when data for a group mark is\
      \ processed for the first time and the \ngroup mark is newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: GroupEncodeEnter
    required: true

```
</details>

### Induced

<details>
```yaml
name: GroupEncode
description: "A set of visual encoding properties that determine the position of a\
  \ group mark, which are used for subplots. \nIn Vega, there are three primary property\
  \ sets: enter, update, exit. The enter properties are evaluated when data \nis processed\
  \ for the first time and a mark instance is newly added to a scene and are the only\
  \ properties \nsupported for a group mark."
from_schema: https://w3id.org/scverse/vega-scverse/specification
rank: 1000
attributes:
  enter:
    name: enter
    description: "Enter properties that are evaluated when data for a group mark is\
      \ processed for the first time and the \ngroup mark is newly added to a scene."
    from_schema: https://w3id.org/scverse/vega-scverse/encode
    alias: enter
    owner: GroupEncode
    domain_of:
    - ImageEncode
    - LabelEncode
    - SymbolEncode
    - PathEncode
    - TextEncode
    - GroupEncode
    range: GroupEncodeEnter
    required: true

```
</details>