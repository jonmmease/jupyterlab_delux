JupyterLab Delux
================
This repo is a proof-of-concept of a conda package that includes JupyterLab
with preinstalled extensions.

Use Cases
=========
Standardized distribution
-------------------------
An organization could create their own build of JupyterLab with a predefined
set of extensions. Note: If users are operating in an online environment, they 
would still be able to add/remove extensions themselves after installation.

Offline Installation
--------------------
A build of JupyterLab with predefined extensions could be installed in an 
offline environment, without requiring nodejs or access to an
npm repository.

Implementation Notes
====================
The package name, in this example, is `jupyterlab_delux` (not `jupyterlab`).
This means that `conda` will treat this as a totally separate package from 
`jupyterlab`.  To keep `conda` from allowing the installation 
of both `jupyterlab_delux` and `jupyterlab` an unsatisfiable 
`run_constrained` condition is imposed.

```yaml
run_constrained:
    - jupyterlab <0.0.0 
```

See: [conda/conda-build#2001](https://github.com/conda/conda-build/pull/2001)

Limitations
===========
This approach does not address the open question of how individual extensions 
should be distributed as conda packages and installed in an offline 
environment.

See [jupyterlab/jupyterlab#2065](https://github.com/jupyterlab/jupyterlab/issues/2065)
for discussion on this front. 

Instructions
============
**Note:** This has only been tested with `conda-build` version 3.0.29

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

Launch JupyterLab
```bash
$ jupyter lab
```

Open `notebooks/test_jupyterlab_delux.ipynb`. Both `ipywidgets` and `bqplot`
extensions should be working without additional intervention  

Acknowledgements
================
This recipe was initially based on the `jupyterlab` conda-forge feedstock from
https://github.com/conda-forge/jupyterlab-feedstock
