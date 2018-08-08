#!/usr/bin/env bash
python -m pip install --no-deps --ignore-installed .

export JUPYTERLAB_DIR=$PREFIX/share/jupyter/delux

# Extensions to install
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install bqplot --no-build
jupyter lab build
jupyter lab clean
