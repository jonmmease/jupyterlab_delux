# JupyterLab {{ cookiecutter.project_name }}

Conda recipe to package JupyterLab with preinstalled extensions.

The package created has two scripts:

* *project_slug*`-lab` equivalent for the bundle to `jupyter lab`
* *project_slug*`-labextension` equivalent for the bundle to `jupyter labextension`

This means that, if the user has `nodejs` installed and internet access, he can manage
extensions as with the standard JupyterLab.

## Use Cases

### Standardized distribution

An organization could create their own build of JupyterLab with a predefined
set of extensions.

Note: If users are operating in an online environment, they 
would still be able to add/remove extensions themselves after installation.
In this case, they will have to specify the `JUPYTERLAB_DIR` variable before
calling `jupyter labextension install my_extenstion` or use the argument `app-dir`:

```bash
jupyter labextension install --app_dir=$CONDA_PREFIX/share/jupyter/delux my_extension
```

### Offline Installation

A build of JupyterLab with predefined extensions could be installed in an 
offline environment, without requiring nodejs or access to an
npm repository.

## Limitations

This approach does not address the open question of how individual extensions 
should be distributed as conda packages and installed in an offline 
environment.

See [jupyterlab/jupyterlab#2065](https://github.com/jupyterlab/jupyterlab/issues/2065)
for discussion on that front.

## Instructions

1. Adapt the template to bundle the extensions you want
    1. Add the JupyterLab extension installation commands in `recipe/bld.bat` and `recipe/build.sh`
    They will have the following structure `jupyter labextension` *extension_name* `--no-build`
    1. Add the Jupyter server extensions needed by the JupyterLab extensions in the `run` section of `recipe/meta.yaml`

1. Generate the conda package

    ```bash
    conda build -c conda-forge recipe
    ```

As displayed by the `conda build` command, this will create a conda package in your `anaconda/conda-bld/noarch` directory.

Comments:

* You can specify JupyterLab extension versions to install using the npm notation *extension_name@version*.
* You can specify JupyterLab and Jupyter server extensions versions using conda notation *package =X.Y.Z* or *package >=X.Y.Z*

Create a fresh environment and then install this package. The `--use-local` flag
tells `conda` to look in the `conda-bld` directory for packages. This step requires
configured `conda` channels, but not `nodejs` or an `npm` repository.

```bash
conda create -n test_{{ cookiecutter.project_slug }}_lab python>=3.5
source activate test_{{ cookiecutter.project_slug }}_lab
conda install jupyterlab_{{ cookiecutter.project_slug }} --use-local
```

Launch JupyterLab with preinstalled extensions

```bash
{{ cookiecutter.project_slug }}-lab
```

Open `notebooks/test_jupyterlab_{{ cookiecutter.project_slug }}.ipynb`. Both `ipywidgets` and `bqplot`
extensions should be working without additional intervention.
