@echo off

SET EXE="%PREFIX%\Scripts\jupyter-serverextension.exe"
if exist %EXE%  (
   %EXE% disable jupyterlab --py --sys-prefix > NUL 2>&1 && if errorlevel 1 exit 1
)