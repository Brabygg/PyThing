from random import randint

intros = (
    "No one knows what may come forth from the Funny Fruit Machine. Push the buttons at your own risk."
)

receives = (
    "The Funny Fruit Machine has blessed you with ",
    "As the smoke clears, you find yourself in possession of ",
    "With a loud 'ping' you are faced with ",
    "A voice thunders 'Here you go, sir' as something magically appears in your hand. Once all the molten lava has been cleaned off, it is indeed "
)

fruit = (
    "a dragonfruit",
    "an eggplant",
    "a Sweet Gem Berry",
    "ambrosia",
    "[observantly] pint apple"
)

def print_fruit(rin, fin):
    print(f"\n{receives[int(rin)]}{fruit[int(fin)]}.")

print("The Funny Fruit Machine")

while True:
    fid = input("Select funny fruit:\n")

    print_fruit(randint(0, len(receives) - 1), int(fid) - 1)

    print("\nWould you like an additional funny fruit? y/n")

    quit = False
    while True:
        res = input()
        if res == "y":
            break
        elif res == "n":
            quit = True
            break
    if quit:
        break