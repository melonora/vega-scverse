# vega-spatialdata

Vega like specification for the scverse plotting ecosystem. Currently, only supports
viewconfigurations for `SpatialData` visualizations. The repository includes pydantic classes
that can be used to validate the viewconfiguration and its available components.

## Website
Documentation on the specification can be found here:
https://melonora.github.io/vega-scverse/

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

### Installing Pixi

This project uses [pixi](https://pixi.sh) for dependency management. To install pixi, follow these steps:

#### Windows
You can download and run the [installer](https://github.com/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi)
or run the following:
```
# Using PowerShell (recommended)
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```
The terminal needs to be restarted to make the installation effective. See details below for what this does.
<details>
The above invocation will automatically download the latest version of pixi, extract it, and move the pixi binary to 
%UserProfile%\.pixi\bin. The command will also add %UserProfile%\.pixi\bin to your PATH environment variable, allowing 
you to invoke pixi from anywhere.
</details>

If you want to turn on autocompletion check the location of your profile by running in the
PowerShell: `$PROFILE`. At the end of this file add the following line:

```(& pixi completion --shell powershell) | Out-String | Invoke-Expression```
#### macOS/Linux
```
# Using curl
curl -fsSL https://pixi.sh/install.sh | sh

# Or using wget if you don't have curl
wget -qO- https://pixi.sh/install.sh | sh
```

Now restart your terminal or shell to make the installation effective. For what this does, see the windows section.
To enable autocompletion, add to your `.bashrc`:
```eval "$(pixi completion --shell bash)"```

### Installing Dependencies

Once pixi is installed, you can install the project dependencies:

```
# Install all dependencies
pixi install -a

# Or install specific environment dependencies:
pixi install -E dev   # Development dependencies
pixi install -E test  # Testing dependencies
pixi install -E doc   # Documentation dependencies
pixi install -E all   # All environments above combined
```

### Activating Environments

After the environment(s) are installed, you can activate a specific environment by entering
the following in your terminal (doc environment in this example):

```pixi shell -e doc```

### Running Tests

To run tests, use:

```
pixi run -e test test
```

### Linting schemas

We run the linkml linter on the schemas. For this we also have a config `.lint_config.yaml` which disables standard 
naming rule. This because the Vega grammar of graphics on which we base the viewconfiguration, does not follow the
standard naming rules as defined in [LinkML](https://linkml.io/). You can run the linter on all schemas as follows:

```shell
pixi run lint
```


## Documentation

To generate and view the documentation locally, one must have pixi installed. Please 
see the developer documentation details above.

If you already have pixi installed, start with ensuring the dependencies are installed.
```
# Install all dependencies
pixi install -a

# Or install only documentation dependencies
pixi install -E doc
```

All documentation-related commands are defined in the doc environment. Because they are unique
to this environment, you don't have to specify or be in the environment to run the commands.
1. Generate the documentation:
   ```
   pixi run gen_doc
   ```

2. View the documentation in a local web server:
   ```
   pixi run serve
   ```

3. Or do both in one command:
   ```
   # Using pixi directly (run these commands in sequence)
   pixi run gen_doc
   pixi run serve
   ```

The documentation will be available at http://localhost:8000 in your web browser. 

Deploying the documentation is not necessary. This is taken care of by a GitHub action.

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
test