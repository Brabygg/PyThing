import classes as c
import random as r
import os
import sys
import json

player = c.Trainer(None, 3000, [], [], [])

def main():
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
    cls()
    print(f"Trainer: {player.name} [${player.money}]")
    print("\nParty:", end=" ")
    i = 0
    for poke in player.party:
        print(f"{poke.nick} ({poke.name} {'♀' if poke.woman else '♂'}){' [SHINY]' if poke.shiny else ''}", end=", " if i + 1 != len(player.party) else "\n")
        i += 1

    print("\n[A] Proceed  [M] Shop  [P] View party summaries  [S] Save and quit")
    while True:
        choice = input().strip().lower()

        if choice == "p":
            print("Input the party member's index...\n[B] Back")
            while True:
                choice = input().strip().lower()
                if choice == "b":
                    print("[A] Proceed  [M] Shop  [P] View party summaries  [S] Save and quit")
                    break

                try:
                    poke_summary(player.party[int(choice) - 1])
                    hub()
                except:
                    continue

        elif choice == "s":
            save_game()
            sys.exit()

def add_poke(poke):
    cls()
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
    cls()
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
    save_file = open("poke.sav", "w")
    save_file.write("")
    save_file.close()

    party = []
    for poke in player.party:

        i = 0
        for element in poke.element:
            poke.element[i] = element.name
            i += 1

        poke.stats = poke.stats.__dict__
    
        party.append(poke.__dict__)

    box = []
    for poke in player.box:

        i = 0
        for element in poke.element:
            poke.element[i] = element.name
            i += 1

        poke.stats = poke.stats.__dict__
    
        box.append(poke.__dict__)

    save_file = open("poke.sav", "a")
    save_file.write(json.dumps([player.name, player.money]))
    save_file.write("\n" + json.dumps(player.inventory))
    save_file.write("\n" + json.dumps(party))
    save_file.write("\n" + json.dumps(box))
    save_file.close()

def cls():
    os.system("cls" if os.name == "nt" else "clear")

main()