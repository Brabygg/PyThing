import classes as c
import random as r

def start_battle():
    poke = c.pokemon_list[r.choice(list(c.pokemon_list.keys()))]
    party = [c.generate_pokemon(poke["id"], poke["name"], poke["name"], poke["type"], poke["stats"])]

    opponent = c.Trainer(r.choice(c.random_names), r.randint(100, 10000), [], party, [])

    return opponent

def battle_hub(player : c.Pokemon, opponent : c.Pokemon):
    player_health = player.stats.hp
    opponent_health = opponent.stats.hp

    while True:
        display_ui(player_health, player, opponent_health, opponent)

        print("\n[A] Attack  [P] Pass turn")
        active = True
        player_damage = 0
        while active:
            choice = input(f"What will {player.nick} do?\n").strip().lower()

            if choice == "a":
                active = False

                player_crit = True if r.randint(1, 15) == 1 else False
                player_damage = calculate_damage(player.stats.attack, opponent.stats.defense, player_crit, 1)

            elif choice == "p":
                active = False
                player_damage = -1

        opponent_crit = True if r.randint(1, 15) == 1 else False
        opponent_damage = calculate_damage(opponent.stats.attack, player.stats.defense, opponent_crit, 1)

        c.cls()

        if (player.stats.speed > opponent.stats.speed) or (player.stats.speed == opponent.stats.speed and r.randint(1, 2) == 1):
            opponent_health -= player_damage

            display_ui(player_health, player, opponent_health, opponent)
            if player_damage != -1:
                input(f"\n{player.nick} used Tackle{' (CRIT!)' if player_crit else ''} and dealt {player_damage} damage!\n")

            if opponent_health > 0:
                player_health -= opponent_damage

                display_ui(player_health, player, opponent_health, opponent)
                input(f"\n{opponent.name} used Tackle{' (CRIT!)' if opponent_crit else ''} and dealt {opponent_damage} damage!\n")

                if player_health <= 0:
                    print(f"{player.nick} fainted!")
                    return False
        
        else:
            player_health -= opponent_damage

            display_ui(player_health, player, opponent_health, opponent)
            input(f"\n{opponent.name} used Tackle{' (CRIT!)' if opponent_crit else ''} and dealt {opponent_damage} damage!\n")

            if player_health > 0:
                opponent_health -= player_damage

                display_ui(player_health, player, opponent_health, opponent)
                if player_damage != -1:
                    input(f"\n{player.nick} used Tackle{' (CRIT!)' if player_crit else ''} and dealt {player_damage} damage!\n")

                if opponent_health <= 0:
                    print(f"{opponent.name} fainted!")
                    return True
                
        if opponent_health <= 0:
            print(f"{opponent.name} fainted!")
            return True
        if player_health <= 0:
            print(f"{player.nick} fainted!")
            return False

def display_ui(player_health, player, opponent_health, opponent):
    c.cls()

    print(f"Enemy: {opponent.name}")
    print_healthbar(opponent_health, opponent.stats.hp)
    print(f"\n\n{player.nick} ({player.name} {'♀' if player.woman else '♂'})")
    print_healthbar(player_health, player.stats.hp)
    print(f"{player_health if player_health > 0 else 0} / {player.stats.hp}")

def print_healthbar(hp, max):
    print("[", end="")
    print(f"{'-' if hp >= max else ' '}", end="")
    print(f"{'-' if hp >= max * 0.9 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.8 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.7 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.6 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.5 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.4 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.3 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.2 else ' '}", end="")
    print(f"{'-' if hp >= max * 0.1 else ' '}", end="")
    print(f"{'-' if hp > 0 else ' '}", end="")
    print("]")

def calculate_damage(attack, defense, crit, effect_mult):
    power = 50

    return round((((22 * power * attack / defense) / 50) * (2 if crit else 1) + 2) * effect_mult * (r.randint(217, 255) / 255))