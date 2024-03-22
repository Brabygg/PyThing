import os

consonant_string = "bcdfghjklmnpqrstvwxz"
consonants = list(consonant_string + consonant_string.upper())

def main():
    os.system("cls" if os.name == "nt" else "clear")

    text = input("Enter a string to convert: ")
    output = run_algorithm(text)
    input(output + "\n")
    main()

def run_algorithm(text):
    new_text = ""
    for char in text:
        if char in consonants:
            new_text += char + "o" + char.lower()
        else:
            new_text += char

    return new_text.capitalize()

main()