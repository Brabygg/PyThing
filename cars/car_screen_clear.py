import os
import platform as pf

def cls():
    if pf.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")