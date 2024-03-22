import os

word = []
revealed = []
used = []

def main():
    global word

    word = list(input("Input the word you'd like to use: ").strip().lower())

    for i in range(len(word)):
        revealed.append("_")

    print(word)

    start_game()

def start_game():
    active = True
    while active:

        os.system("cls" if os.name == "nt" else "clear")

        word_string = ""
        for char in revealed:
            word_string += f" {char} "

        used_string = ""
        for char in used:
            used_string += f" {char} "

        print(f"Current status:{word_string}")
        print(f"Used letters:{used_string}")
        char = input("Your guess: ")
        if len(char) != 1:
            continue

        used.append(char)
        if not char in word:
            continue

        while char in word:
            index = word.index(char)

            revealed[index] = word[index]
            word[index] = "_"

        if not "_" in revealed:
            active = False

    print(f"The word was {''.join(revealed).upper()}! You won!")
    input()
    main()

main()