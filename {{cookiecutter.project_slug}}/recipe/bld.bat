%PYTHON% -m pip install --no-deps --ignore-installed .

SET JUPYTERLAB_DIR=%PREFIX%\share\jupyter\{{ cookiecutter.project_slug }}

REM Extensions to install
SET NODE_OPTIONS=--max-old-space-size=16000
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install bqplot --no-build
jupyter lab build
jupyter lab clean
if errorlevel 1 exit 1
