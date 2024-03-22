import os

def main():
    while True:
        res = input("Input the sentence whose letters you'd like to count: ").strip().upper()
        out = count_letters(res)
        
        for letter in out:
            print(letter + ": " + str(out[letter]))

        input()
        os.system("cls" if os.name == "nt" else "clear")

def count_letters(string):
    letters = {}
    for char in string:
        count = string.count(char)
        if count != 0 and char != " ":
            letters[char] = count

    letters = dict(sorted(letters.items()))
    
    return letters

main()