#!/usr/bin/env bash
$PYTHON -m pip install --no-deps --ignore-installed .

export JUPYTERLAB_DIR=$PREFIX/share/jupyter/delux

# Extensions to install
export NODE_OPTIONS=--max-old-space-size=16000
# Add below the extensions you want to package
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install bqplot --no-build
jupyter lab build
jupyter lab clean
