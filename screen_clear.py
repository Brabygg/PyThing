import os
import platform as pf

def cls():
    if pf.uname() == "Windows":
        os.system("cls")
    else:
        os.system("clear")