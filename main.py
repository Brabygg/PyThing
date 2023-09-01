from random import randint

res = input("Pick a random number from 1 - 65 536: ")
if (int(res) == randint(1, 65536)):
    print("Somehow, you were actually correct! Congrats!")
else:
    print("WRONG!")
input()