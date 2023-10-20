import database as db
import os
import sys

connection, cursor = db.connect_to_database('words.db')
target = 'english'

def main():
    cls()
    print("THE FUNNY WORD PRACTICE THING, WHERE YOU CAN PRACTICE WORDS AND ALSO DO OTHER THINGS LIKE CHANGE WHICH WORDS TO PRACTICE")
    print("THIS PROGRAM USES A DATABASE AND IS VERY COOL AND GOOD AND FUNNY AND OTHER POSITIVE ADJECTIVES")
    print("---\n")
    top_menu()

def top_menu():
    print("1 - Practice words\n2 - Manage word lists\n3 - Manage languages\n4 - Quit")
    res = input("What would you like to do?\n").strip()
    if res == "1":
        # Start word practice
        pass
    elif res == "2":
        edit_list()
    elif res == "3":
        edit_tables()
    elif res == "4":
        db.close_connection(connection, cursor)
        sys.exit()
    else:
        cls()
        top_menu()

def edit_list():
    cls()
    print(f"Currently active word list: {target}, contents:")
    print_table(target)
    print("\n1 - Add a word pair | 2 - Remove a word pair | 3 - Back")

    res = input("What would you like to do?\n").strip()
    if res == "1":

        cls()
        native = input("Input the word in your native language: ")
        trans = input(f"Input the word in the target language ({target}): ")
        e_c = db.add_to_table(cursor, connection, target, native.strip(), trans.strip())

        if e_c == 0:
            input("\nDATABASE STATUS -- SUCCESS\nPress ENTER to continue:\n")
            edit_list()
        else:
            print("\nDATABASE STATUS -- ERROR\nYou may have input an invalid value, or the database is not present on your system.")
            input("Press ENTER to exit:\n")
            db.close_connection(connection)
            sys.exit()
        
    elif res == "2":
        active = True
        while active:
            select = input("Enter the ID of the value to remove: ").strip()
            try:
                select = int(select)
                active = False
            except:
                pass

        e_c = db.remove_from_table(cursor, connection, target, int(select))
        
        if e_c == 0:
            input("\nDATABASE STATUS -- SUCCESS\nPress ENTER to continue:\n")
            edit_list()
        else:
            print("\nDATABASE STATUS -- ERROR\nYou may have input an invalid value, or the database is not present on your system.")
            input("Press ENTER to exit:\n")
            db.close_connection(connection)
            sys.exit()

    elif res == "3":
        cls()
        top_menu()

    else:
        edit_list()

def edit_tables():
    cls()
    print(f"Currently active word list: {target}\nAvailable tables:\n")
    print_dbs()
    print("Input the name of a word list to set it as active, in addition:")
    print("1 - Add a new word list | 2 - Remove a word list | 3 - Back")

    res = input("What would you like to do?")
    if res == "1":
        name = input("Give the word list a name: ")
        e_c = db.create_table(cursor, connection, name)

        if e_c == 0:
            target = name
            input("\nDATABASE STATUS -- SUCCESS\nNew word list set as active, press ENTER to continue:\n")
            edit_list()
        else:
            print("\nDATABASE STATUS -- ERROR\nYou may have input an invalid value, or the database is not present on your system.")
            input("Press ENTER to exit:\n")
            db.close_connection(connection)
            sys.exit()

    elif res == "2":
        active = True:
        while active:
            select = input("Enter the name of the word list to delete: ")


def print_table(table):
    entries = db.list_table_entries(cursor, table)

    for entry in entries:
        print(f"ID {entry[0]}: {entry[1]} -- {entry[2]}")
    print("\n")

def print_dbs():
    entries = db.list_all_tables(cursor)

    for entry in entries:
        print(entry[0])
    print("\n")

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

main()