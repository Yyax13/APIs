import os
import yollor
import sys

def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def sair():
    sys.exit(os.system('cls' if os.name == 'nt' else 'clear'))
