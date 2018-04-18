#!/usr/bin/env bash
python -m pip install --no-deps --ignore-installed .
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install bqplot
