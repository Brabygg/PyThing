from random import randint

rand_num = randint(1, 10000)
correct = False

res = input("Pick a random number from 1 - 10000. You get ten guesses: ")
for i in range(9):
    res = int(res)
    if (res == rand_num):
        print("Somehow, you were actually correct! Congrats.")
        correct = True
        input()
        break
    else:
        print(f"WRONG! {9 - i} guess{ '' if 9 - i == 1 else 'es' } left.")
        print(f"(Hint: the number you're looking for is {'HIGHER' if rand_num > res else 'LOWER'})")
        res = input("Continue: ")

if (correct == False):
    print(f"You are a fucking pathetic loser. Can't even get a 1/1000 chance to guess {rand_num}? Get out of my sight, maggot.")
    input()