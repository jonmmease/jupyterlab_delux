python -m pip install --no-deps --ignore-installed .

SET JUPYTERLAB_DIR=%PREFIX%\share\jupyter\delux

REM Extensions to install
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.35 --no-build
jupyter labextension install bqplot@0.3 --no-build
jupyter lab build
jupyter lab clean
if errorlevel 1 exit 1
