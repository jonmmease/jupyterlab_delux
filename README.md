JupyterLab Delux
================

This repo is a proof-of-concept of a conda package that includes JupyterLab
with preinstalled extensions.

Use Cases
=========

Standardized distribution
-------------------------

An organization could create their own build of JupyterLab with a predefined
set of extensions. 

Note: If users are operating in an online environment, they 
would still be able to add/remove extensions themselves after installation.
In this case, they will have to specify the `JUPYTERLAB_DIR` variable before
calling `jupyter labextension install my_extenstion` or use the argument `app-dir`:

```bash
jupyter labextension install --app_dir=$CONDA_PREFIX/share/jupyter/delux my_extension
```


Offline Installation
--------------------

A build of JupyterLab with predefined extensions could be installed in an 
offline environment, without requiring nodejs or access to an
npm repository.

Implementation Notes
====================

The package name, in this example, is `jupyterlab_delux` (not `jupyterlab`).
`jupyterlab` is a dependency of this package. To have a clear separation between
the standard `jupyterlab` and this version with preinstalled extensions, we take
advantage of the `LabApp.app_dir` configurable property (see the 
[documentation](http://jupyterlab.readthedocs.io/en/stable/user/extensions.html#advanced-usage)).

That parameter is more easily specified through the environment variable `JUPYTERLAB_DIR`.
In this case JUPYTERLAB_DIR=$CONDA_PREFIX\share\jupyter\delux.

To launch easily this customized JupyterLab, an entry point is created to call `jupyterlab_delux:main`.

Limitations
===========

This approach does not address the open question of how individual extensions 
should be distributed as conda packages and installed in an offline 
environment.

See [jupyterlab/jupyterlab#2065](https://github.com/jupyterlab/jupyterlab/issues/2065)
for discussion on that front. 

Instructions
============

**Note:** This has only been tested with `conda-build` version 3.10.9

Build the package in an online environment as follows:

```bash
$ conda build recipe/
```

As displayed by the `conda build` command, this will create a conda package in 
your `anaconda/conda-bld/noarch` directory

Create a fresh environment and then install this package. The `--use-local` flag
tells `conda` to look in the `conda-bld` directory for packages. This step requires
configured `conda` channels, but not `nodejs` or an `npm` repository.

```bash
$ conda create -n test_jupyterlab_delux python=3.6
$ source activate test_jupyterlab_delux
$ conda install jupyterlab_delux --use-local
```

Launch JupyterLab with preinstalled extensions
```bash
$ jupyterlab_delux
```

Open `notebooks/test_jupyterlab_delux.ipynb`. Both `ipywidgets` and `bqplot`
extensions should be working without additional intervention  

Customization
=============

Bundled extensions are specified in `jupyter labextension install {extension_name} --no-build` commands in 
`recipe/build.sh` (and `recipe/bld.bat` for Windows). 
Python packages corresponding the these extensions are specified as `run` requirements in `recipe/meta.yaml`.

The folder hosting the JupyterLab with preinstalled extensions is specified by the variable environment
in `recipe/build.sh` (and `recipe/bld.bat`) and in `jupyterlab_delux:main` to create an entry point.
