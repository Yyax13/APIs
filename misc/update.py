import os
import subprocess
from misc import loading as Carregante

def pip(package):
    try:
        subprocess.check_output(["pip", "show", package])
        print(f'{package} already installed')
    except subprocess.CalledProcessError:
        os.system(f'pip install {package}')
        print(f'Done')
