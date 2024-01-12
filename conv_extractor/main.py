import tkinter as tk
import sys
import os

root = tk.Tk()
root.title("Conversation Extractor")
root.geometry("500x150")

def main():
    clear()

    title_label = tk.Label(text="Chat Extractor // Person Remover // Conversation Scissor // IDK\n---")
    title_label.grid(row=0, sticky=tk.N)
    button_container = tk.Frame()
    button_container.grid(row=1, sticky=tk.N)
    tutorial_button = tk.Button(button_container, text="?", command=open_tutorial)
    tutorial_button.grid(row=0, sticky=tk.W)
    start_button = tk.Button(button_container, text="Begin", command=start_read)
    start_button.grid(row=0, column=1, sticky=tk.N)
    exit_button = tk.Button(button_container, text="Quit", command=sys.exit)
    exit_button.grid(row=0, column=2, sticky=tk.E)
    dev_label = tk.Label(text="---\nDeveloped by QUADRATIC // Made with Tkinter, unfortunately")
    dev_label.grid(row=2, sticky=tk.S)

    root.mainloop()

def clear():
    items = root.winfo_children()
    for item in items:
        item.destroy()

def open_tutorial():
    tutorial_text = """Place the desired file in the bundled "input" directory.
    It must follow a format where one person's message occupies one line:
    PERSON1: I like dragons
    PERSON2: Shut up, dragonlover
    PERSON3: I don't know what else to put here, you get the idea
    After the conversion is complete, the resulting file will appear in the "output" directory."""
    clear()

    tutorial_label = tk.Label(text=tutorial_text)
    tutorial_label.grid(sticky=tk.E)
    back_button = tk.Button(text="Return", command=main)
    back_button.grid(row=1, sticky=tk.S)

def start_read():
    files = os.listdir("input/")
    clear()

    dir_label = tk.Label()
    dir_label.grid(sticky=tk.N)
    button_container = tk.Frame()
    button_container.grid(row=1)
    confirm_button = tk.Button(button_container, text="Confirm", command=lambda: get_users(files[0]))
    cancel_button = tk.Button(button_container, text="Cancel", command=main)

    if len(files) == 0:
        dir_label.config(text="No files detected in input directory.\nPlease place the file you'd like to use there, and try again.")
        cancel_button.grid(sticky=tk.S)
    else:
        dir_label.config(text=f"File detected: {files[0]}\n(if this is not the desired file, remove all others from the input directory)")
        confirm_button.grid(row=0, column=1, sticky=tk.E)
        cancel_button.grid(row=0, sticky=tk.W)

def get_users(file_path):
    file = open(f"input/{file_path}", encoding="utf-8-sig")
    data = file.readlines()
    file.close()
    users = []

    for line in data:
        user = line[0:line.index(":")]
        if user not in users:
            users.append(user)

    user_list = ""
    for user in users:
        user_list += user + "\n"

    clear()

    users_label = tk.Label(text=f"Detected users in document:\n\n{user_list}\nInput user to extract:")
    users_label.grid(sticky=tk.N)
    input_container = tk.Frame()
    input_container.grid(row=1, sticky=tk.S)
    user_input = tk.Entry(input_container)
    user_input.grid(row=0, sticky=tk.W)
    confirm_button = tk.Button(input_container, text="Go", command=lambda: extract_file(file_path, users, user_input.get()))
    confirm_button.grid(row=0, column=1, sticky=tk.E)

def extract_file(file_path, users, user):
    if user not in users:
        return
    
    file = open(f"input/{file_path}", encoding="utf-8-sig")
    data = file.readlines()
    file.close()

    i = 0
    for line in data:
        line_user = line[0:line.index(":")]
        if line_user == user:
            data.pop(i)
        i += 1

    output_files = os.listdir("output/")
    output_index = 1
    while f"output{output_index}.txt" in output_files:
        output_index += 1
    
    output = open(f"output/output{output_index}.txt", "a")
    for line in data:
        output.write(line)

    clear()

    info_label = tk.Label(text=f"Operation successful.\nResult saved as output{output_index}.")
    info_label.grid(sticky=tk.N)
    back_button = tk.Button(text="Return", command=main)
    back_button.grid(row=1, sticky=tk.S)

main()