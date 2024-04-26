import classes as c
import battles as b
import random as r
import pickle as p
import os
import sys

player = c.Trainer(None, 3000, [], [], [])
opponent = None

def main():
    from_save = False

    if os.path.isfile("./poke.sav"):
        if input("Save file 'poke.sav' found. Would you like to load it? (y/n)\n").strip().lower() == "y":
            from_save = True
            load_game()
            hub()

    if from_save:
        return

    while True:
        player.name = input("Enter your name: ").strip()
        if player.name == "":
            print(f"How about {r.choice(c.random_names)}?")
            continue
        break

    print("Choose a starter:")

    i = 1
    for pokemon in c.pokemon_list.keys():
        print(f"{i}: {pokemon}")
        i += 1

    while True:
        choice = input().strip()
        try:
            if int(choice) <= 0 or int(choice) > i - 1:
                continue
            break
        except:
            continue

    name = list(c.pokemon_list.keys())[int(choice) - 1]
    select = c.pokemon_list[name]
    starter = c.generate_pokemon(select["id"], name, name, select["type"], select["stats"])

    add_poke(starter)
    hub()

def hub():
    c.cls()
    print(f"Trainer: {player.name} [${player.money}]")
    print("\nParty:", end=" ")
    i = 0
    for poke in player.party:
        print(f"{poke.nick} ({poke.name} {'♀' if poke.woman else '♂'}){' [SHINY]' if poke.shiny else ''}", end=", " if i + 1 != len(player.party) else "\n")
        i += 1

    print("\n[A] Proceed  [M] Shop  [P] View party summaries  [S] Save and quit")
    active = True
    while active:
        choice = input().strip().lower()

        if choice == "a":
            active = False

            c.cls()
            opponent = b.start_battle()
            enemy = opponent.party[0]
            print(f"{opponent.name} wants to battle!\n{opponent.name} sent out {enemy.name}!")
            input()

            fighter = player.party[0]

            b.battle_hub(fighter.stats.hp, fighter, enemy.stats.hp, enemy)

            input("Something happened, I guess")

        elif choice == "p":
            print("Input the party member's index...\n[B] Back")
            while active:
                choice = input().strip().lower()
                if choice == "b":
                    print("[A] Proceed  [M] Shop  [P] View party summaries  [S] Save and quit")
                    break

                try:
                    poke_summary(player.party[int(choice) - 1])
                    active = False
                    hub()
                except:
                    continue

        elif choice == "s":
            save_game()

def battle_win():
    prize = round(opponent.money / 2)

    input(f"{player.name} defeated {opponent.name} and received ${prize}!\n")
    player.money += prize
    hub()

def battle_loss():
    prize = round(player.money / 2)

    input(f"{player.name} was defeated by {opponent.name} and paid ${prize} to the winner...\n")
    player.money -= prize
    hub()

def add_poke(poke):
    c.cls()
    print(f"You got {poke.name}!\nGive it a nickname? (y/n)")
    while True:
        choice = input().strip().lower()

        if choice == "y":
            while True:
                poke.nick = input(f"Input a nickname for {poke.name} ({'♀' if poke.woman else '♂'}): ").strip()
                if poke.nick == "":
                    print(f"How about {r.choice(c.random_names)}?")
                    continue
                break
            break
        elif choice == "n":
            break

    if len(player.party) < 6:
        player.party.append(poke)
    else:
        player.box.append(poke)

def poke_summary(poke):
    c.cls()
    print("= = = SUMMARY = = =")
    print(f"{poke.nick} ({poke.name} {'♀' if poke.woman else '♂'})")
    if poke.shiny:
        print("SHINY")
    print("\nTypes:")
    for element in poke.element:
        print(c.Types(element).name)
    print("\nStats:")
    print(f"HP: {poke.stats.hp}\nAttack: {poke.stats.attack}\nDefense: {poke.stats.defense}\nSp. Atk.: {poke.stats.sp_atk}\nSp. Def.: {poke.stats.sp_def}\nSpeed: {poke.stats.speed}")
    print(f"{list(c.natures.keys())[list(c.natures.values()).index(poke.nature)]} nature ({f'{poke.nature[0]} up, {poke.nature[1]} down' if poke.nature[0] != poke.nature[1] else 'neutral'})")
    input("\nPress ENTER to continue...\n")

def save_game():
    print("Saving game...")

    with open("poke.sav", "wb") as file:
        p.dump(player, file)

    print("Save complete, closing shortly.")

    sys.exit()

def load_game():
    global player

    with open("poke.sav", "rb") as file:
        player = p.load(file)

    print(player.name)

main()