python -m pip install --no-deps --ignore-installed .

REM Get Python sys.prefix
FOR /F "tokens=* USEBACKQ" %%F IN (`python -c "import sys; print(sys.prefix)"`) DO (
    SET JUPYTERLAB_DIR=%%F\share\jupyter\delux
)

REM Extensions to install
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install bqplot --no-build
jupyter lab build
jupyter lab clean
if errorlevel 1 exit 1
