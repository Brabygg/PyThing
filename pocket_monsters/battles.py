import classes as c
import random as r

def start_battle():
    poke = c.pokemon_list[r.choice(list(c.pokemon_list.keys()))]
    party = [c.generate_pokemon(poke["id"], poke["name"], poke["name"], poke["type"], poke["stats"])]

    opponent = c.Trainer(r.choice(c.random_names), r.randint(100, 10000), [], party, [])

    return opponent

def battle_hub(player_health, player, opponent_health, opponent):
    c.cls()

    print(f"Enemy: {opponent.name}")
    print_healthbar(opponent_health, opponent.stats.hp)
    print(f"\n\n{player.nick} ({player.name} {'♀' if player.woman else '♂'})")
    print_healthbar(player_health, player.stats.hp)
    print(f"{player_health} / {player.stats.hp}")

    print("\n[A] Attack")
    active = True
    player_damage = 0
    while active:
        choice = input(f"What will {player.nick} do?\n").strip().lower()

        if choice == "a":
            active = False
            player_damage = calculate_damage(player.stats.attack, opponent.stats.defense, True if r.randint(1, 15) == 1 else False, 1)

    opponent_damage = calculate_damage(opponent.stats.attack, player.stats.defense, True if r.randint(1, 15) == 1 else False, 1)

    c.cls()

    if (player.stats.speed > opponent.stats.speed) or (player.stats.speed == opponent.stats.speed and r.randint(1, 2) == 1):
        opponent_health -= player_damage

        print(f"Enemy: {opponent.name}")
        print_healthbar(opponent_health, opponent.stats.hp)
        print(f"\n\n{player.nick} ({player.name} {'♀' if player.woman else '♂'})")
        print_healthbar(player_health, player.stats.hp)
        print(f"{player_health} / {player.stats.hp}")
        input(f"\n{player.nick} used Tackle and dealt {player_damage} damage!\n")

        if opponent_health > 0:
            player_health -= opponent_damage

            c.cls()

            print(f"Enemy: {opponent.name}")
            print_healthbar(opponent_health, opponent.stats.hp)
            print(f"\n\n{player.nick} ({player.name} {'♀' if player.woman else '♂'})")
            print_healthbar(player_health, player.stats.hp)
            print(f"{player_health} / {player.stats.hp}")
            input(f"\n{opponent.name} used Tackle and dealt {opponent_damage} damage!\n")

            if player_health > 0:
                battle_hub(player_health, player, opponent_health, opponent)
    
    else:
        player_health -= opponent_damage

        print(f"Enemy: {opponent.name}")
        print_healthbar(opponent_health, opponent.stats.hp)
        print(f"\n\n{player.nick} ({player.name} {'♀' if player.woman else '♂'})")
        print_healthbar(player_health, player.stats.hp)
        print(f"{player_health} / {player.stats.hp}")
        input(f"\n{opponent.name} used Tackle and dealt {opponent_damage} damage!\n")

        if player_health > 0:
            opponent_health -= player_damage

            c.cls()

            print(f"Enemy: {opponent.name}")
            print_healthbar(opponent_health, opponent.stats.hp)
            print(f"\n\n{player.nick} ({player.name} {'♀' if player.woman else '♂'})")
            print_healthbar(player_health, player.stats.hp)
            print(f"{player_health} / {player.stats.hp}")
            input(f"\n{player.nick} used Tackle and dealt {player_damage} damage!\n")

            if opponent_health > 0:
                battle_hub(player_health, player, opponent_health, opponent)

    if opponent_health <= 0:
        print(f"{opponent.name} fainted!")
    elif player_health <= 0:
        print(f"{player.nick} fainted!")

def print_healthbar(hp, max):
    print("[", end="")
    print(f"{'---' if hp >= max else '   '}", end="")
    print(f"{'---' if hp >= max * 0.75 else '   '}", end="")
    print(f"{'---' if hp >= max * 0.5 else '   '}", end="")
    print(f"{'---' if hp > 0 else '   '}", end="")
    print("]")

def calculate_damage(attack, defense, crit, effect_mult):
    power = 50

    return round((((22 * power * attack / defense) / 50) * (2 if crit else 1) + 2) * effect_mult * (r.randint(217, 255) / 255))