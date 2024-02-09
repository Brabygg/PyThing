import loc
import things
import random as r

map_x = 10
map_y = 10
enemy_chance = 10
item_chance = 10

map = None

def main():
    global map

    map = loc.create_map(map_x, map_y, enemy_chance, item_chance)
    move_to_room(r.randint(0, map_x - 1), r.randint(0, map_y - 1), None)

def display_map(cur_x, cur_y):
    output = "["
    x_index = 0
    y_index = 0
    for room in map:
        if room.x == cur_x and room.y == cur_y:
            output += " # "
        else:
            output += " + "

        x_index += 1
        if x_index == map_x and y_index < map_y:
            output += "]\n["
            x_index == 0
            y_index += 1
        elif y_index == map_y:
            output += "]"

    print(output)

def move_to_room(x, y, dir):
    target_room = None

    for room in map:
        if room.x == x and room.y == y:
            target_room = room
            break

    if dir == None:
        print("You find yourself in a nondescript room.")
    else:
        new_text = r.choice(things.new_room)
        print(new_text[0] + dir + new_text[1])

    print("\n1: NORTH\n2: SOUTH\n3: EAST\n4: WEST\nFor further commands, type \"help\".")

    while True:
        command = input("What do you do?\n").strip()
        
        if command == "1":
            if y - 1 < 0:
                print("There is nothing in that direction.")
                continue
            move_to_room(x, y - 1, "north")
        elif command == "2":
            if y + 1 >= map_y:
                print("There is nothing in that direction.")
                continue
            move_to_room(x, y + 1, "south")
        elif command == "3":
            if x + 1 >= map_x:
                print("There is nothing in that direction.")
                continue
            move_to_room(x + 1, y, "east")
        elif command == "4":
            if x - 1 < 0:
                print("There is nothing in that direction.")
                continue
            move_to_room(x - 1, y, "west")

        elif command == "help":
            print("\n'map' -- Display the map.")
        elif command == "map":
            display_map(x, y)

main()