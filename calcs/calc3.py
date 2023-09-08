import os
from math import *

while True:
    os.system("cls")
    i = input("Enter expression...\n")
    try:
        print("\nAnswer: " + str(eval(i)))
    except ZeroDivisionError:
        print("\nMany attempts throughout history have been made to define division by zero.\nThis calculator is not one of those.")
    except Exception as e:
        print("Error: " + str(e))
    print("\n1 - Continue | 2 - Quit")

    quit = False
    while True:
        res = input()
        if res == "1":
            break
        elif res == "2":
            quit = True
            break
    if quit:
        break