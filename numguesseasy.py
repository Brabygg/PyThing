from random import randint

rand_num = randint(1, 10)
correct = False

prizes = [
    "a live grenade",
    "authentic Siberian ice, stored in a pizza oven",
    "pizza, encased in Siberian ice",
    "a violin (bow not included)",
    "a free oxygen atom",
    "a spare Alloush",
    "a year's supply of antimatter (antimatter-proof containment not included)",
    "a lifetime supply of auto-installing Windows updates"
]

res = input("Pick a random number from 1 - 10. You get three guesses: ")
for i in range(2):
    res = int(res)
    if res == rand_num:
        print("Somehow, you were actually correct! Congrats.")
        print(f"Here's your prize: {prizes[randint(0, len(prizes) - 1)]}!")
        correct = True
        input()
        break
    else:
        print(f"WRONG! {2 - i} guess{ '' if 2 - i == 1 else 'es' } left.")
        print(f"(Hint: the number you're looking for is {'HIGHER' if rand_num > res else 'LOWER'})")
        res = input("Continue: ")

res = int(res)
if res == rand_num and not correct:
    print("Somehow, you were actually correct! Congrats.")
    print(f"Here's your prize: {prizes[randint(0, len(prizes) - 1)]}!")
    correct = True
    input()

if not correct:
    print(f"You are a fucking pathetic loser. Can't even get a ~1/3 chance to guess {rand_num}? Get out of my sight, maggot.")
    input()