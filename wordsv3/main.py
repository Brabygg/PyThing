import database as db
import sys
from random import randint, choice
import tkinter as tk
import atexit

top_menu_splashes = [
    "Please don't use this program to recreate 9/11.\nI dunno how you would actually do that, but don't.",
    "What's that behind you?",
    "Hey, your hair looks nice today. New cut?",
    "Get some more practice in. Please. I don't want my process to die.",
    "Translate 'bollar' to English:",
    "Accusations of the developer being a furry are baseless, and they find it greatly insulting.",
    "'Nya~ :3'\n  // The developer",
    "Also try Wordlings v2!",
    "The developer explaining why a program like this needs a main menu splash screen:\n(it doesn't)",
    "Sponsored: Redeem a free ticket for American Airlines Flight 11 TODAY by visiting\nhttps://brabygg.github.io/LEGITGIVEAWAY/LEGITGIVEAWAY.html",
    "tk.Button(button_container, width=20, height=1, text='Back', command=top_menu)"
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

root = tk.Tk()
root.title("Word Practice Assistant // Developed by Brabygg")
root.geometry("475x150")


connection, cursor = db.connect_to_database('words.db')
target = "English"

def main():
    cls()
    print("Word Practice Assistant")
    print("Developed by Nils K // Brabygg")
    print("---\n")
    top_menu()

def top_menu():
    cls()

    splash_label = tk.Label(root, text=f"{choice(top_menu_splashes)}\n---", width=65, height=5)
    splash_label.grid(row=0, column=0, sticky=tk.N)

    button_container = tk.Frame(root, width=80)
    button_container.grid(row=1, column=0, sticky=tk.N)
    practice_button = tk.Button(button_container, width=15, height=1, text="Practice Words", command=start_practice)
    practice_button.grid(row=1, column=0, sticky=tk.W)
    list_button = tk.Button(button_container, width=15, height=1, text="Manage Word Lists", command=edit_list)
    list_button.grid(row=1, column=1, sticky=tk.N)
    lang_button = tk.Button(button_container, width=15, height=1, text="Manage Languages", command=edit_tables)
    lang_button.grid(row=1, column=2, sticky=tk.E)

    root.mainloop()

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
        no_list_label = tk.Label(root, text="You have not created or selected a word list to use with the program.\nWould you like to do this now?")
        no_list_label.grid(sticky=tk.N)
        button_container = tk.Frame(root)
        button_container.grid(row=1, sticky=tk.N)
        yes_button = tk.Button(button_container, width=10, height=1, text="Yes", command=edit_list)
        yes_button.grid(row=0, column=0, sticky=tk.W)
        no_button = tk.Button(button_container, width=10, height=1, text="No", command=top_menu)
        no_button.grid(row=0, column=1, sticky=tk.N)

    match_found = False
    tables = db.list_all_tables(cursor)

    for table in tables:
        if target == table[0]:
            match_found = True

    if not match_found:
        no_list_label = tk.Label(root, text=f"Word list '{target}' does not exist, possibly due to being removed.\nPlease select or create a different one.\nWould you like to do this now?")
        no_list_label.grid(sticky=tk.N)
        button_container = tk.Frame(root)
        button_container.grid(row=1, sticky=tk.N)
        yes_button = tk.Button(button_container, width=10, height=1, text="Yes", command=edit_list)
        yes_button.grid(row=0, column=0, sticky=tk.W)
        no_button = tk.Button(button_container, width=10, height=1, text="No", command=top_menu)
        no_button.grid(row=0, column=1, sticky=tk.N)

    for word in db.list_table_entries(cursor, target):
        words.append(word)

    if len(words) == 0:
        no_list_label = tk.Label(root, text=f"Word list '{target}' is empty. Please add words to it in order to use it.\nWould you like to do this now?")
        no_list_label.grid(sticky=tk.N)
        button_container = tk.Frame(root)
        button_container.grid(row=1, sticky=tk.N)
        yes_button = tk.Button(button_container, width=10, height=1, text="Yes", command=edit_list)
        yes_button.grid(row=0, column=0, sticky=tk.W)
        no_button = tk.Button(button_container, width=10, height=1, text="No", command=top_menu)
        no_button.grid(row=0, column=1, sticky=tk.N)

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

    top_label = tk.Label(text=f"Currently active word list: {target}, contents:")
    top_label.grid(sticky=tk.N)
    print_table(target)
    button_container = tk.Frame(root)
    button_container.grid(row=999, sticky=tk.N)
    add_button = tk.Button(button_container, width=20, height=1, text="Add a Word Pair", command=open_add_to_list)
    add_button.grid(row=0, column=0, sticky=tk.W)
    back_button = tk.Button(button_container, width=20, height=1, text="Back", command=top_menu)
    back_button.grid(row=0, column=1, sticky=tk.N)

def open_add_to_list():
    cls()

    back_button = tk.Button(root, text="Back", command=edit_list)
    back_button.grid(sticky=tk.W)
    add_container = tk.Frame(root)
    add_container.grid(sticky=tk.N)
    native_label = tk.Label(add_container, text="Input the word in your native language:")
    native_label.grid(row=1, sticky=tk.N)
    native_input = tk.Entry(add_container)
    native_input.grid(row=2, sticky=tk.N)
    trans_label = tk.Label(add_container, text=f"Input the word in the target language ({target}):")
    trans_label.grid(row=3, sticky=tk.N)
    trans_input = tk.Entry(add_container)
    trans_input.grid(row=4, sticky=tk.N)
    confirm_button = tk.Button(root, text="Submit", command=lambda: add_to_list(native_input.get(), trans_input.get(), status_display=status_label))
    confirm_button.grid(row=5, sticky=tk.N)
    status_label = tk.Label(root)
    status_label.grid(row=6, sticky=tk.N)

def add_to_list(native, trans, status_display):

    native = native.strip().lower()
    trans = trans.strip().lower()

    e_c = db.add_to_table(cursor, connection, target, native, trans)

    if e_c == 0:
        status_display.config(text=f"Success! Word pair '{native} -- {trans}' added to list '{target}'.")
        
    elif e_c == 2:
        pass

    else:
        status_display.config(text=f"ERROR: Database operation failed. Please try again.")

def remove_entry(id):
    print("Removing entry " + str(id))

    e_c = db.remove_from_table(cursor, connection, target, id)

    if e_c == 0:
        edit_list()
    else:
        status_label = tk.Label(root, text="ERROR: Database operation failed. Please try again.")
        status_label.grid(sticky=tk.N)

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
    labels = []
    buttons = []

    for entry in entries:
        labels.append(tk.Label(text=f"{entry[1]} -- {entry[2]}"))
        buttons.append(tk.Button(text="Remove"))

    i = 0
    for entry in entries:
        labels[i].grid(row=i+1, sticky=tk.N)
        buttons[i].grid(row=i+1, column=1, sticky=tk.W)
        buttons[i].config(command=lambda: remove_entry(entry[0]), text=entry[0])
        i += 1

    #print(buttons[0].cget("command"))

def print_dbs():
    entries = db.list_all_tables(cursor)

    for entry in entries:
        print(entry[0])
    print("\n")

def cls():
    for widget in root.winfo_children():
        widget.destroy()

def capture_exit():
    db.close_connection(connection, cursor)

atexit.register(capture_exit)

main()