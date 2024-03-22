import os

the_number = 21
players = []

print("The Number of Doom is at 21.")
print("Players will take turns to subtract a value between one and five from the number.")
print("The player who reduces the Number of Doom to zero will unleash hell itself upon reality,\ndestroying their corporeal form in the process.")
print("Good luck.")

def main():
    try:
        player_count = int(input("Enter the game's player count (at least two): ").strip())
        if player_count < 2:
            main()
    except:
        main()

    for i in range(player_count):
        players.append(input(f"Player {i + 1}, what shall be your title?\n"))

    cur_turn = 0
    while the_number > 0:
        player_turn(players[cur_turn])

        if the_number > 0:
            cur_turn += 1
            if cur_turn >= len(players):
                cur_turn = 0

    print(f"{players[cur_turn]} has reduced the Number of Doom to zero,\nsubsequently erasing themselves from existence in one fell swoop.")
    print("All remaining life should consider themselves lucky to have not been swept away by the current of destruction.")
    input("Press ENTER to make another attempt...\n")
    main()

def player_turn(player):
    global the_number

    os.system("cls")
    print(f"The Number of Doom is {the_number}.")
    sub = 0
    try:
        sub = int(input(f"{player}, select the amount you'd like to subtract.\n"))
        if sub < 1 or sub > 5:
            sub = 0
            player_turn(player)
        the_number -= sub
    except:
        player_turn(player)

            

main()