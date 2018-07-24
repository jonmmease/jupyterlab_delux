#!/usr/bin/env bash
python -m pip install --no-deps --ignore-installed .

# Get Python sys.prefix
PYTHON_PREFIX=`python -c "import sys; print(sys.prefix)"`
export JUPYTERLAB_DIR=$JUPYTERLAB_DIR/share/jupyter/delux

# Extensions to install
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install bqplot --no-build
jupyter lab build
jupyter lab clean
