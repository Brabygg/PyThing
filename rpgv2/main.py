import classes
import things
import random as r
import os

map_x = 10
map_y = 10
enemy_chance = 10
item_chance = 10
wall_chance = 25

player = classes.player(100, 100, [], 0)

map = None

def main():
    global map

    while True:
        map = classes.create_map(map_x, map_y, item_chance, wall_chance)
        move_to_room(r.randint(0, map_x - 1), r.randint(0, map_y - 1), None)

def display_map(cur_x, cur_y):
    output = "["
    x_index = 0
    y_index = 0
    for room in map:
        if room.x == cur_x and room.y == cur_y:
            output += " @ "
        elif room.seen and room.wall:
            output += " # "
        elif room.visited:
            output += " + "
        else:
            output += " ? "

        x_index += 1
        if x_index == map_x: 
            if y_index < map_y - 1:
                output += "]\n["
                x_index = 0
                y_index += 1
            else:
                output += "]"
                break

    print(output)

def display_inv():
    print("-- CURRENT STATUS --")
    print(f"Health: {player.health}/{player.max_health}")
    if len(player.inventory) == 0:
        print("Inventory empty.")
    else:
        print("Inventory:")
        for item in player.inventory:
            print(f"- {item}")
    print(f"Kills: {player.kills}\n")

def move_to_room(x, y, dir):

    target_room = None

    if x < 0 or x > map_x - 1 or y < 0 or y > map_y - 1:
        print("There is nothing in that direction.")
        return

    for room in map:
        if room.x == x and room.y == y and room.wall:
            print(r.choice(things.wall_block))
            return

    i = 0
    target_found = False
    for room in map:
        if room.x == x and room.y == y:
            target_found = True
        if (room.x == x and (room.y == y or room.y == y + 1 or room.y == y - 1))\
        or (room.x == x - 1 and (room.y == y or room.y == y + 1 or room.y == y - 1))\
        or (room.x == x + 1 and (room.y == y or room.y == y + 1 or room.y == y - 1)):
            room.seen = True
        if not target_found:
            i += 1

    map[i].visited = True

    os.system("cls" if os.name == "nt" else "clear")

    if dir == None:
        print("You find yourself in a nondescript room.\n")
    else:
        new_text = r.choice(things.new_room)
        print(new_text[0] + dir + new_text[1] + "\n")

    if r.randint(0, 100) <= enemy_chance:
        new_text = r.choice(things.enemy_encounter)
        new_enemy = r.choice(things.enemies)
        print(new_text[0] + new_enemy + new_text[1])
        begin_combat(new_enemy, r.randint(1, 15))        

    if map[i].item != None:
        new_text = r.choice(things.item_pickup)
        print(new_text[0] + map[i].item + new_text[1])
        player.inventory.append(map[i].item)
        map[i].item = None
    
    display_map(x, y)

    print("\n1: NORTH\n2: SOUTH\n3: EAST\n4: WEST\nFor further commands, type \"help\".")

    while True:
        command = input("What do you do?\n").strip().lower()

        if command == "1":
            move_to_room(x - 1, y, "north")
        elif command == "2":
            move_to_room(x + 1, y, "south")
        elif command == "3":
            move_to_room(x, y + 1, "east")
        elif command == "4":
            move_to_room(x, y - 1, "west")

        elif command == "help":
            print("\n'map' -- Display the map.\n'inv' -- Display player status.")
        elif command == "map":
            display_map(x, y)
        elif command == "inv":
            display_inv()

def begin_combat(enemy, strength):
    print(f"You are fighting a {enemy}.")

    enemy_health = strength * 15
    enemy_damage = strength * 5

    active = True
    while active:
        print("1: STRIKE\n2: DEFEND\n3: FLEE")

    command = input("What do you do?").strip().lower()

    if command == "1":
        enemy_health -= 30 * r.random() + 1
    elif command == "2":
        pass
    elif command == "3":
        pass

main()