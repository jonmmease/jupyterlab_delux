import os
import sys
from jupyterlab import labapp
 

def main():
    os.environ['JUPYTERLAB_DIR'] = os.path.join(sys.prefix, 'share', 'jupyter', 'delux')
    labapp.LabApp.app_dir = os.environ['JUPYTERLAB_DIR']
    labapp.main()
    
    
if __name__ == '__main__':
    sys.exit(main())
