# Vega-scverse

Welcome to the official documentation for Vega-scverse, a specialized framework that provides a Vega-like specification for the scverse plotting ecosystem.

![Vega-SpatialData Logo](https://via.placeholder.com/150)

## Introduction

Vega-scverse is designed to standardize and simplify the creation of visualizations for spatial data in the single-cell analysis domain. It provides a declarative approach to defining visualizations, making it easier to create, share, and reproduce complex visualizations of spatial data.

## Key Features

- **Declarative Visualization Specification**: Define visualizations using a JSON-based specification language
- **SpatialData Integration**: Seamless integration with the SpatialData format
- **Validation Framework**: Built-in validation using Pydantic models
- **Extensible Design**: Easily extend with new visualization components
- **Interoperability**: Works with other tools in the scverse ecosystem

## Getting Started

### Installation

```bash
pip install vega_scverse
```

### Basic Usage

```python
from vega_scverse import ViewConfiguration

# Create a view configuration
view_config = ViewConfiguration(
    # Configuration parameters
)

# Use with your SpatialData object
# ...
```

## Documentation Structure
TBD 
## Examples

TBD

## Community and Support

- **GitHub**: [Report issues and contribute](https://github.com/melonora/vega-scverse)
- **Discourse**: [Join discussions](https://discourse.scverse.org/)

## Citation

If you use Vega-scverse in your research, please cite:

```
@software{vega_spatialdata,
  author = {Vierdag, Wouter-Michiel and Contributors},
  title = {Vega-scverse: A Vega-like specification for plotting / visualization in the scverse ecosystem.},
  url = {https://github.com/melonora/vega-scverse},
  year = {2025}
}
```