from random import randint

prizes = [
    "one million U.S dollars (subject to 103% income tax)",
    "ownership rights to a 2cu.m. patch of empty space in low solar orbit",
    "a spare kidney",
    "Diezel's big sausage, between two buns",
    "the N-word pass",
    "every current Stellaris DLC",
    "a body pillow of a dragon",
    "a license for getting stabbed",
    "one trillion Turkish lira",
    "the perfect guide to learn HTML2"
]

def get_prize(count):
    if count > len(prizes):
        raise Exception(f"No more than {len(prizes)} draws allowed")
    
    previous_num = []
    wins = []

    for i in range(count):
        looping = True
        while looping:
            num = randint(0, len(prizes) - 1)
            if previous_num.count(num) == 0:
                looping = False
        
        if randint(1, 50) == 1:
            previous_num.append(num)
            wins.append(prizes[num])

    return wins
        