import os

the_alphabet = ["A", "B", "C", "D", "E", "F",
                "G", "H", "I", "J", "K", "L", 
                "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X",
                "Y", "Z", "Å", "Ä", "Ö"]

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def advance_cipher(string):
    new_string = []

    for char in string:
        is_upper = char.isupper()
        char = char.upper()

        try:
            i = the_alphabet.index(char)
        except ValueError:
            new_string.append(char)
            continue
        
        new_char = the_alphabet[(i + 1) % len(the_alphabet)]

        if not is_upper:
            new_char = new_char.lower()

        new_string.append(new_char)

    return ''.join(new_string)

def remove_zeros(number):
    number = float(number)
    if number.is_integer():
        return str(int(number))
    return str(number)

def coin_input():
    price = int(input("Cost of what you'd like to buy (in cents): "))
    one_coins = int(input("Number of pennies: "))
    five_coins = int(input("Number of nickels: "))
    ten_coins = int(input("Number of dimes: "))
    twenty_five_coins = int(input("Number of quarters: "))

    return coin_calculator([one_coins, five_coins, ten_coins, twenty_five_coins], price)

def coin_calculator(coin_array, price):
    # [0] - 1, [1] - 5, [2] - 10, [3] - 25

    total = 0
    total += coin_array[0]
    total += coin_array[1] * 5
    total += coin_array[2] * 10
    total += coin_array[3] * 25

    if total < price:
        return False
    return True