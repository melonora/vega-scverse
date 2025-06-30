# vega-spatialdata

Vega like specification for the scverse plotting ecosystem.

## Website

[https://scverse.github.io/vega-spatialdata](https://scverse.github.io/vega-spatialdata)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [vega_scverse](src/vega_scverse)
    * [schema](src/vega_scverse/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/vega_scverse/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
To run commands you may use good old make or the command runner [just](https://github.com/casey/just/) which is a better choice on Windows.
Use the `make` command or `duty` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
</details>

## Documentation

To generate and view the documentation locally:

> **IMPORTANT**: All commands must be run through pixi. Do not run commands like `mkdocs` directly from the command line, as they will not be found. Always use `pixi run mkdocs` instead.

First, make sure you have installed the dependencies:
```
# Install all dependencies
pixi install

# Or install only documentation dependencies
pixi install -E doc
```

1. Generate the documentation:
   ```
   # Using make
   make gendoc

   # Using just
   just _gendoc

   # Using pixi directly
   pixi run gen-doc
   ```

2. View the documentation in a local web server:
   ```
   # Using make
   make serve

   # Using just
   just _serve

   # Using pixi directly
   pixi run mkdocs serve
   ```

3. Or do both in one command:
   ```
   # Using make
   make testdoc

   # Using just
   just testdoc

   # Using pixi directly (run these commands in sequence)
   pixi run gen-doc
   pixi run mkdocs serve
   ```

The documentation will be available at http://localhost:8000 in your web browser.

## Troubleshooting

### Command not found errors

If you see an error like this:
```
mkdocs : The term 'mkdocs' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

This means you're trying to run a command directly that is only available through pixi. Always prefix these commands with `pixi run`:

```
pixi run mkdocs serve
```

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
