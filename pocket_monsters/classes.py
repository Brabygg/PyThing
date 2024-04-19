from random import randint, choice
from enum import Enum
import os

class Types(Enum):
    NORMAL = 1
    FIGHTING = 2
    FLYING = 3
    FIRE = 4
    WATER = 5
    GRASS = 6
    ELECTRIC = 7
    POISON = 8
    ROCK = 9
    GROUND = 10
    BUG = 11
    GHOST = 12
    PSYCHIC = 13
    ICE = 14
    DRAGON = 15
    STEEL = 16
    DARK = 17

class Stats:
    def __init__(self, hp : int, attack : int, defense : int, sp_atk : int, sp_def : int, speed : int):
        self.hp = hp
        self.attack  = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed

class Pokemon:
    def __init__(self, id : int, name : str, nick : str, element : list, stats : Stats, woman : bool, shiny : bool, nature : list):
        self.id = id
        self.name = name
        self.nick = nick
        self.element = element
        self.stats = stats
        self.woman = woman
        self.shiny = shiny
        self.nature = nature

def generate_pokemon(id : int, name : str, nick : str, element : list, stats : Stats):
    woman = True if randint(1, 2) == 1 else False
    shiny = True if randint(1, 8192) == 1 else False
    
    nature = natures[choice(list(natures.keys()))]
    if nature[0] == "attack":
        stats.attack *= 1.1
    if nature[0] == "defense":
        stats.defense *= 1.1
    if nature[0] == "sp_atk":
        stats.sp_atk *= 1.1
    if nature[0] == "sp_def":
        stats.sp_def *= 1.1
    if nature[0] == "speed":
        stats.speed *= 1.1

    if nature[1] == "attack":
        stats.attack *= 0.9
    if nature[1] == "defense":
        stats.defense *= 0.9
    if nature[1] == "sp_atk":
        stats.sp_atk *= 0.9
    if nature[1] == "sp_def":
        stats.sp_def *= 0.9
    if nature[1] == "speed":
        stats.speed *= 0.9

    stats.attack = round(stats.attack)
    stats.defense = round(stats.defense)
    stats.sp_atk = round(stats.sp_atk)
    stats.sp_def = round(stats.sp_def)
    stats.speed = round(stats.speed)

    return Pokemon(id, name, nick, element, stats, woman, shiny, nature)

class Trainer:
    def __init__(self, name : str, money : int, inventory : list, party : list, box : list):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.party = party
        self.box = box

random_names = [
    'Adie', 'Amid', 'Amin', 'Amir', 'Angie', 'Ashleigh', 'Ashton', 'Aubrey', 'Barnes',
    'Barry', 'Basil', 'Bernadine', 'Bethany', 'Braden', 'Bradley',
    'Brent', 'Bret', 'Brett', 'Burdine', 'Caden','Cadence', 'Carrington',
    'Charlene', 'Charles', 'Charlton', 'Chay', 'Daris', 'Darleen', 'Darlene',
    'Darnell', 'Deb', 'Demi', 'Dennis', 'Diamond', 'Diezel', 'Doreen', 'Dorothy',
    'Dustin', 'Earlene', 'Elaine', 'Elfriede', 'Emery', 'Emory', 'Evan',
    'Gabriel', 'Georgiana', 'Gladys', 'Greenbury', 'Gregory', 'Greig',
    'Gwen', 'Harley', 'Hastings', 'Hazel', 'Heather', 'Helton', 'Henrietta',
    'Heston', 'Holly', 'Hulda', 'India', 'Irene', 'Jackie', 'Jade', 'January',
    'Jemma', 'Jenny', 'Jerald', 'Jerrold', 'Jerry', 'Jessie', 'Jethro', 'Jigar',
    'Jill', 'Jocelyn', 'Jodie', 'Joey', 'Justine', 'Kate', 'Kathryn', 'Keaton',
    'Kendra', 'Kerr', 'Kimball', 'Kitty', 'Kristy', 'Kylie', 'Laren', 'Lawrence',
    'Lawson', 'Leanne', 'Lianne', 'Louise', 'Luci', 'Maddox', 'Malford', 'Marlene',
    'Maud', 'Melinda', 'Melville', 'Mindy', 'Molly', 'Mort', 'Nancy', 'Nelson',
    'Nigel', 'Osbert', 'Ottilie', 'Pamela', 'Pascoe', 'Percy', 'Piper', 'Pippa',
    'Poppy', 'Raleigh', 'Rebecca', 'Reynold', 'Rhoda', 'Riley', 'Roland', 'Rosaleen',
    'Rosalie', 'Rosie', 'Ruby', 'Rupert', 'Ruth', 'Savannah', 'Scarlett', 'Sharon',
    'Sheridan', 'Shiloh', 'Sidney', 'Stacy', 'Sue', 'Sven', 'Sydney', 'Tammy', 'Tim',
    'Timmy', 'Timothy', 'Tracy', 'Travis', 'Trent', 'Trudie', 'Tucker', 'Velma',
    'Vicary', 'Violet', 'Walker', 'Warren', 'Whitney', 'Wilfried', 'Woodrow'
]

natures = {
    "Hardy":["attack", "attack"],
    "Lonely":["attack", "defense"],
    "Brave":["attack", "speed"],
    "Adamant":["attack", "sp_atk"],
    "Naughty":["attack", "sp_def"],
    "Bold":["defense", "attack"],
    "Docile":["defense", "defense"],
    "Relaxed":["defense", "speed"],
    "Impish":["defense", "sp_atk"],
    "Lax":["defense", "sp_def"],
    "Timid":["speed", "attack"],
    "Hasty":["speed", "defense"],
    "Serious":["speed", "speed"],
    "Jolly":["speed", "sp_atk"],
    "Naive":["speed", "sp_def"],
    "Modest":["sp_atk", "attack"],
    "Mild":["sp_atk", "defense"],
    "Quiet":["sp_atk", "speed"],
    "Bashful":["sp_atk", "sp_atk"],
    "Rash":["sp_atk", "sp_def"],
    "Calm":["sp_def", "attack"],
    "Gentle":["sp_def", "defense"],
    "Sassy":["sp_def", "speed"],
    "Careful":["sp_def", "sp_atk"],
    "Quirky":["sp_def", "sp_def"]
}

pokemon_list = {
    "Bulbasaur":{
        "name":"Bulbasaur",
        "id":1,
        "type":[Types.GRASS, Types.POISON],
        "stats":Stats(45, 49, 49, 65, 65, 45)
    },
    "Pikachu":{
        "name":"Pikachu",
        "id":25,
        "type":[Types.ELECTRIC],
        "stats":Stats(35, 55, 30, 50, 40, 90)
    },
    "Magneton":{
        "name":"Magneton",
        "id":82,
        "type":[Types.ELECTRIC, Types.STEEL],
        "stats":Stats(50, 60, 95, 120, 70, 70)
    },
    "Magikarp":{
        "name":"Magikarp",
        "id":129,
        "type":[Types.WATER],
        "stats":Stats(20, 10, 55, 15, 20, 80)
    },
    "Eevee":{
        "name":"Eevee",
        "id":133,
        "type":[Types.NORMAL],
        "stats":Stats(55, 55, 50, 45, 65, 55)
    },
    "Vaporeon":{
        "name":"Vaporeon",
        "id":134,
        "type":[Types.WATER],
        "stats":Stats(130, 65, 60, 110, 95, 65)
    },
    "Dragonair":{
        "name":"Dragonair",
        "id":148,
        "type":[Types.DRAGON],
        "stats":Stats(61, 84, 65, 70, 70, 70)
    },
    "Mareep":{
        "name":"Mareep",
        "id":179,
        "type":[Types.ELECTRIC],
        "stats":Stats(55, 40, 40, 65, 45, 35)
    },
    "Wobbuffet":{
        "name":"Wobbuffet",
        "id":202,
        "type":[Types.PSYCHIC],
        "stats":Stats(190, 33, 58, 33, 58, 33)
    }
}

def cls():
    os.system("cls" if os.name == "nt" else "clear")