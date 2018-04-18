#!/usr/bin/env bash
python -m pip install --no-deps --ignore-installed .

# Extensions to install
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install bqplot
