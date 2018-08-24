JupyterLab Bundle
=================

Cookiecutter template to generate conda package of Jupyterlab with prepackaged extensions independent of a standard JupyterLab installation.
The package created has two scripts:

* *project_slug*`-lab` equivalent for the bundle to `jupyter lab`
* *project_slug*`-labextension` equivalent for the bundle to `jupyter labextension`

Requirements
------------

To generate a recipe, you will need to install `cookiecutter`.

Using `conda`:

```bash
conda install -c conda-forge cookiecutter
```

To generate the JupyterLab bundle, you will need `conda` package manager
and `conda-build` package builder.

Using `conda`:

```bash
conda install -c conda-forge conda-build
```

Usage
-----

1. Generate a new recipe from the cookiecutter template:  

    ```bash
    cookiecutter gh:measejm1/jupyterlab_delux
    ```

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

Implementation Notes
--------------------

To have a clear separation between the standard `jupyterlab` and the version bundled with preinstalled extensions, we take advantage of the `LabApp.app_dir` configurable property (see the 
[documentation](http://jupyterlab.readthedocs.io/en/stable/user/extensions.html#advanced-usage)).

That parameter is more easily specified through the environment variable `JUPYTERLAB_DIR` as you can see in the building scripts.

To launch easily this customized JupyterLab, two entry points are created:

* *project_slug*`-lab` calling `jupyterlab_`*project_slug*`.labapp:main` equivalent for the bundle to `jupyter lab`
* *project_slug*`-labextension` calling `jupyterlab_`*project_slug*`.labextensionapp:main` equivalent for the bundle to `jupyter labextension`

Limitations
-----------

This approach does not address the open question of how individual extensions should be distributed as conda packages and installed in an offline environment.

See [jupyterlab/jupyterlab#2065](https://github.com/jupyterlab/jupyterlab/issues/2065)
for discussion on that front.

License
-------

This project is licensed under the terms of the [BSD 3-Clause License](/LICENSE).

References
----------

* [JupyterLab](https://jupyterlab.readthedocs.io/en/stable)
* [conda packaging](https://conda.io/docs/user-guide/tasks/building-packages/index.html)