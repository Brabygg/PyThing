import classes as c

def main():
    print("pick youre fighter")

    i = 1
    for pokemon in c.pokemon_list.keys():
        print(f"{i}: {pokemon}")
        i += 1

    while True:
        choice = input().strip()
        if int(choice) <= 0 or int(choice) > i - 1:
            continue
        break

    choice = input(f"You got {list(c.pokemon_list.keys())[int(choice) - 1]}!\nGive it a nickname? (y/n)")


main()