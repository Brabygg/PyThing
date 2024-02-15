import loc
import things
import random as r

map_x = 10
map_y = 10
enemy_chance = 10
item_chance = 10
wall_chance = 25

generating = True

map = None

def main():
    global map

    while True:
        map = loc.create_map(map_x, map_y, enemy_chance, item_chance, wall_chance)
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

def move_to_room(x, y, dir):
    global generating

    target_room = None

    if x < 0 or x > map_x - 1 or y < 0 or y > map_y - 1:
        print("There is nothing in that direction.")
        return

    for room in map:
        if room.x == x and room.y == y and room.wall:
            if not generating:
                print(r.choice(things.wall_block))
            return

    generating = False

    for room in map:
        if room.x == x and room.y == y:
            room.visited = True
        if (room.x == x and (room.y == y or room.y == y + 1 or room.y == y - 1))\
        or (room.x == x - 1 and (room.y == y or room.y == y + 1 or room.y == y - 1))\
        or (room.x == x + 1 and (room.y == y or room.y == y + 1 or room.y == y - 1)):
            target_room = room
            room.seen = True

    if dir == None:
        print("You find yourself in a nondescript room.")
    else:
        new_text = r.choice(things.new_room)
        print(new_text[0] + dir + new_text[1])

    if target_room.enemy != None:
        new_text = r.choice(things.enemy_encounter)
        print(new_text[0] + target_room.enemy + new_text[1])

    print("\n1: NORTH\n2: SOUTH\n3: EAST\n4: WEST\nFor further commands, type \"help\".")

    while True:
        command = input("What do you do?\n").strip()
        
        if command == "1":
            move_to_room(x - 1, y, "north")
        elif command == "2":
            move_to_room(x + 1, y, "south")
        elif command == "3":
            move_to_room(x, y + 1, "east")
        elif command == "4":
            move_to_room(x, y - 1, "west")

        elif command == "help":
            print("\n'map' -- Display the map.")
        elif command == "map":
            display_map(x, y)

main()