

# Class: TableObject 


_AnnData Table object stream._





URI: [vega_scverse:TableObject](https://w3id.org/scverse/vega-scverse/TableObject)






```mermaid
 classDiagram
    class TableObject
    click TableObject href "../TableObject"
      DataObject <|-- TableObject
        click DataObject href "../DataObject"
      
      TableObject : format
        
          
    
        
        
        TableObject --> "1" Format : format
        click Format href "../Format"
    

        
      TableObject : name
        
      TableObject : source
        
      TableObject : transform
        
      
```





## Inheritance
* [DataObject](DataObject.md)
    * **TableObject**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [source](source.md) | 1 <br/> [String](String.md) | The source of the SpatialData element | direct |
| [transform](transform.md) | 1..* <br/> [String](String.md)&nbsp;or&nbsp;<br />[FilterTransform](FilterTransform.md) | An array containing a single transform 'filter_element' with an expression st... | direct |
| [name](name.md) | 1 <br/> [String](String.md) | The name used throughout the view configuration to refer to the data object | [DataObject](DataObject.md) |
| [format](format.md) | 1 <br/> [Format](Format.md) | Format object containing the type of data as object and a string value repres... | [DataObject](DataObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/scverse/vega-scverse/specification




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vega_scverse:TableObject |
| native | vega_scverse:TableObject |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TableObject
description: AnnData Table object stream.
from_schema: https://w3id.org/scverse/vega-scverse/specification
is_a: DataObject
attributes:
  source:
    name: source
    description: "The source of the SpatialData element. Must be the name / identifier\
      \ of a SpatialData Object in the \nview configuration."
    from_schema: https://w3id.org/scverse/vega-scverse/data
    rank: 1000
    domain_of:
    - TableObject
    - SpatialDataElementObject
    required: true
    pattern: ^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
  transform:
    name: transform
    description: 'An array containing a single transform ''filter_element'' with an
      expression stating which table to obtain

      from the source SpatialData object stream.'
    from_schema: https://w3id.org/scverse/vega-scverse/data
    rank: 1000
    domain_of:
    - TableObject
    - SpatialDataElementObject
    required: true
    multivalued: true
    exactly_one_of:
    - range: FilterTransform

```
</details>

### Induced

<details>
```yaml
name: TableObject
description: AnnData Table object stream.
from_schema: https://w3id.org/scverse/vega-scverse/specification
is_a: DataObject
attributes:
  source:
    name: source
    description: "The source of the SpatialData element. Must be the name / identifier\
      \ of a SpatialData Object in the \nview configuration."
    from_schema: https://w3id.org/scverse/vega-scverse/data
    rank: 1000
    alias: source
    owner: TableObject
    domain_of:
    - TableObject
    - SpatialDataElementObject
    range: string
    required: true
    pattern: ^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
  transform:
    name: transform
    description: 'An array containing a single transform ''filter_element'' with an
      expression stating which table to obtain

      from the source SpatialData object stream.'
    from_schema: https://w3id.org/scverse/vega-scverse/data
    rank: 1000
    alias: transform
    owner: TableObject
    domain_of:
    - TableObject
    - SpatialDataElementObject
    range: string
    required: true
    multivalued: true
    exactly_one_of:
    - range: FilterTransform
  name:
    name: name
    description: "The name used throughout the view configuration to refer to the\
      \ data object. It is an arbitrary string \nfollowed by an underscore and pseudo\
      \ UUID."
    from_schema: https://w3id.org/scverse/vega-scverse/data
    rank: 1000
    alias: name
    owner: TableObject
    domain_of:
    - DataObject
    - Scale
    range: string
    required: true
    pattern: ^(.*_)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$
  format:
    name: format
    description: Format object containing the type of data as object and a string
      value representing the version.
    from_schema: https://w3id.org/scverse/vega-scverse/data
    rank: 1000
    alias: format
    owner: TableObject
    domain_of:
    - DataObject
    range: Format
    required: true

```
</details>