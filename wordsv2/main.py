import database as db
import os
import sys
from random import randint, choice

top_menu_splashes = [
    "Please don't use this program to recreate 9/11.\nI dunno how you would actually do that, but don't.",
    "What's that behind you?",
    "Hey, your hair looks nice today. New cut?",
    "cls()\ndisplay_splash()\ntop_menu()",
    "Get some more practice in. Please. I don't want my process to die.",
    "Translate 'bollar' to English:",
    "Accusations of the developer being a furry are baseless, and they find it greatly insulting.",
    "'Nya~ :3'\n  // The developer",
    "Also try Wordlings v2!",
    "The developer explaining why a program like this needs a main menu splash screen:\n(it doesn't)",
    "Sponsored: Redeem a free ticket for American Airlines Flight 11 TODAY by visiting\nhttps://brabygg.github.io/LEGITGIVEAWAY/LEGITGIVEAWAY.html"
]

new_list_suggestions = [
    "Language" + str(randint(1, 5)),
    "List" + str(randint(1, 5)),
    "Balls",
    "My Word List",
    "Unnamed 0",
    "Untitled",
    "9/11 Vocabulary",
    "En Passant Jokes"
]

connection, cursor = db.connect_to_database('words.db')
target = None

def main():
    cls()
    print("Word Practice Assistant")
    print("Developed by Nils K // Brabygg")
    print("---\n")
    top_menu()

def top_menu():
    print("1 - Practice words\n2 - Manage word lists\n3 - Manage languages\n4 - Quit")
    res = input("What would you like to do?\n").strip()
    if res == "1":
        start_practice()
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

def display_splash():
    print(choice(top_menu_splashes))
    print("---\n")

def start_practice():
    global target

    cls()
    words = []
    length = 0
    guesses = 0

    if target == None:
        res = input("You have not created or selected a word list to use with the program.\nWould you like to do this now?\n1 - Yes | 2 - No\n").strip()
        if res == "1":
            edit_tables()
        elif res == "2":
            cls()
            display_splash()
            top_menu()
        else:
            start_practice()

    match_found = False
    tables = db.list_all_tables(cursor)

    for table in tables:
        if target == table[0]:
            match_found = True

    if not match_found:
        res = input(f"Word list '{target}' does not exist, possibly due to being removed. Please select or create a different one.\nWould you like to do this now?\n1 - Yes | 2 - No\n").strip()
        if res == "1":
            target = None
            edit_tables()
        elif res == "2":
            cls()
            display_splash()
            top_menu()
        else:
            start_practice()


    for word in db.list_table_entries(cursor, target):
        words.append(word)

    if len(words) == 0:
        res = input(f"Word list '{target}' is empty. Please add words to it in order to use it.\nWould you like to do this now?\n1 - Yes | 2 - No\n").strip()
        if res == "1":
            edit_list()
        elif res == "2":
            cls()
            display_splash()
            top_menu()
        else:
            start_practice()

    length = len(words)

    while len(words) > 0:
        word = choice(words)
        res = input(f"Translate '{word[1]}' to {target}: ").strip().lower()
        if res == word[2]:
            print("Correct!\n")
            words.remove(word)
        else:
            print("Incorrect.\n")
        guesses += 1

    input(f"You have correctly guessed all {length} words in {guesses} guesses!\nPress ENTER to continue:\n")
    cls()
    display_splash()
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
        e_c = db.add_to_table(cursor, connection, target, native.strip().lower(), trans.strip().lower())

        if e_c == 0:
            input("\nDATABASE STATUS -- SUCCESS\nPress ENTER to continue:\n")
            edit_list()
        else:
            print("\nDATABASE STATUS -- ERROR\nYou may have input an invalid value, or the database is not present on your system.")
            input("Press ENTER to exit:\n")
            db.close_connection(connection)
            sys.exit()
        
    elif res == "2":
        while True:
            select = input("Enter the ID of the word pair to remove: ").strip()
            try:
                e_c = db.remove_from_table(cursor, connection, target, int(select))
            except:
                continue
        
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
        display_splash()
        top_menu()

    else:
        edit_list()

def edit_tables():
    global target

    cls()
    print(f"Currently active word list: '{target}'\nAvailable lists:\n")
    print_dbs()
    print("Input the name of a word list to set it as active; in addition:")
    print("1 - Add a new word list | 2 - Remove a word list | 3 - Back")

    res = input("What would you like to do?\n")
    if res == "1":
        name = input("Give the word list a name: ")
        if name == "1" or name == "2" or name == "3":
            input(f"That value is reserved for system functions and not permitted for use. How about '{choice(new_list_suggestions)}'?\nPress ENTER to continue:\n")
            edit_tables()
        e_c = db.create_table(cursor, connection, name.capitalize())

        if e_c == 0:
            target = name.capitalize()
            input("\nDATABASE STATUS -- SUCCESS\nNew word list set as active, press ENTER to continue:\n")
            edit_tables()
        else:
            print("\nDATABASE STATUS -- ERROR\nYou may have input an invalid value, or the database is not present on your system.")
            input("Press ENTER to exit:\n")
            db.close_connection(connection)
            sys.exit()

    elif res == "2":
        while True:
            select = input("Enter the name of the word list to delete: ")

            e_c = db.drop_table(cursor, connection, select)
        
            if e_c == 0:
                input("\nDATABASE STATUS -- SUCCESS\nPress ENTER to continue:\n")
                edit_tables()
            else:
                print("\nDATABASE STATUS -- ERROR\nYou may have input an invalid value, or the database is not present on your system.")
                input("Press ENTER to exit:\n")
                db.close_connection(connection)
                sys.exit()

    elif res == "3":
        cls()
        display_splash()
        top_menu()

    else:
        match_found = False
        tables = db.list_all_tables(cursor)

        for table in tables:
            if res.capitalize() == table[0]:
                match_found = True

        if match_found:
            target = res.capitalize()
            cls()
            input(f"DATABASE STATUS -- SUCCESS\nWord list '{target}' set as active, press ENTER to continue:\n")
            edit_tables()
        else:
            edit_tables()
            

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