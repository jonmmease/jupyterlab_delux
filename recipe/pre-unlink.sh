server_extension="${PREFIX}/bin/jupyter-serverextension"
if [ -x $server_extension ]; then
    ${server_extension} disable jupyterlab --py --sys-prefix > /dev/null 2>&1
fi