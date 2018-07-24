import os
import sys
from jupyterlab.labapp import LabApp


def main():
    os.environ['JUPYTERLAB_DIR'] = os.path.join(sys.prefix, 'share', 'jupyter', 'delux')        
    LabApp.app_dir = os.environ['JUPYTERLAB_DIR']
    LabApp.launch_instance()
    
if __name__ == '__main__':
    main()
