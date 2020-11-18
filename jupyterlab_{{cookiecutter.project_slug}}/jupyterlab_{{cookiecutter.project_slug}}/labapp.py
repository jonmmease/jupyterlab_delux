import os
import sys
from jupyterlab import labapp
 

def main():
    os.environ['JUPYTERLAB_DIR'] = os.path.join(sys.prefix, 'share', 'jupyter', '{{ cookiecutter.project_slug }}')
    labapp.LabApp.app_dir.default_value = os.environ['JUPYTERLAB_DIR']
    labapp.main()
    
    
if __name__ == '__main__':
    sys.exit(main())
