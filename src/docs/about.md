# About Vega-SpatialData

## Project Overview

Vega-scverse is a specialized framework that provides a Vega-like specification for the scverse plotting ecosystem. It is designed to standardize and simplify the creation of visualizations for spatial data in the single-cell analysis domain.

## Key Features

- **Viewconfigurations for SpatialData**: Currently focused on supporting viewconfigurations for `SpatialData` visualizations
- **Validation Framework**: Includes Pydantic classes that can be used to validate viewconfigurations and their components
- **LinkML Schema**: Uses LinkML for schema definition, ensuring interoperability and extensibility
- **Standardized Visualization**: Provides a consistent approach to visualizing spatial data across the scverse ecosystem

## Deviations from Vega

While a lot of the terminology within the specification is essentially Vega, we for now had to deviate in particular 
circumstances. The main reason for this is that in Vega there is currently no support for bioimaging data or single-cell
related datastructures such as [AnnData](https://anndata.readthedocs.io/en/stable/). This means that for those parts of 
specification dealing with data specific terminology, we had to create our own terminology for the specification.
Our long term goal is to reduce this gap with [Vega](https://vega.github.io/vega/docs/specification/).

## Purpose

The primary goal of Vega-scverse is to bring the power and flexibility of Vega-like declarative visualization specifications to the spatial single-cell analysis domain. By providing a standardized way to define visualizations, it enables researchers to:

1. Create reproducible visualizations
2. Share visualization configurations easily
3. Integrate with other tools in the scverse ecosystem
4. Customize visualizations without deep programming knowledge

## Technical Foundation

The project is built on:

- **Python**: Requires Python 3.10 or newer
- **Pydantic**: For data validation and settings management
- **LinkML**: For schema definition and generation of data models

## Development and Contribution

Vega-SpatialData is an open-source project that welcomes contributions. The development workflow uses:

- **Pixi**: For dependency management
- **GitHub**: For version control and collaboration
- **MkDocs**: For documentation

## License

Vega-SpatialData is licensed under the BSD-3 License, making it freely available for both academic and commercial use.

## Authors

The project is maintained by Wouter-Michiel Vierdag (michiel.vierdag@scverse.org) and contributors from the scverse community.

## Acknowledgments

This project was created using the [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter) template.
We would like to acknowledge the help of the Vega development team, in particular @[mattijn](https://github.com/mattijn) for always answering any 
questions we had related to [Vega](https://vega.github.io/vega/docs/specification/). 
Much of the specification is pretty much Vega.

## Fiscal Sponsorship

anndata is part of the scverse® project ([website](https://scverse.org), [governance](https://scverse.org/about/roles)) and is fiscally sponsored by [NumFOCUS](https://numfocus.org/).
If you like scverse® and want to support our mission, please consider making a tax-deductible [donation](https://numfocus.org/donate-to-scverse) to help the project pay for developer time, professional services, travel, workshops, and a variety of other needs.

<div align="center">
<a href="https://numfocus.org/project/scverse">
  <img
    src="https://raw.githubusercontent.com/numfocus/templates/master/images/numfocus-logo.png"
    width="200"
  >
</a>
</div>
