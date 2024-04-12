from random import randint
from enum import Enum

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
    PSYCHIC= 13
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
    def __init__(self, id : int, name : str, nick : str, element : list, stats : Stats):
        self.id = id
        self.woman = True if randint(1, 2) == 1 else False
        self.shiny = True if randint(1, 8192) == 1 else False
        self.name = name
        self.nick = nick
        self.element = element
        self.stats = stats

class Trainer:
    def __init__(self, name : str, inventory : list, party : list):
        self.name = name
        self.inventory = inventory
        self.party = party

trainer_name_list = ['AdieÆthelburg', 'Angie', 'AshleighAshton', 'AubreyBarnes',
                      'Barry', 'Basil', 'BernadineBethany', 'Braden', 'Bradley', 'Brent',
                      'Bret', 'BrettFMOUPages in category "English given names"ABBurdineCaden',
                      'Cadence', 'Carrington', 'Charlene', 'CharlesCharlton', 'Chay', 'DarisDarleenDarlene',
                      'DarnellDeb', 'DemiDennisDiamond', 'Doreen', 'Dorothy', 'Dustin', 'EarleneElaine',
                      'ElfriedeEmery', 'Emory', 'EvanGabriel', 'GeorgianaGladys', 'GreenburyGregory', 'Greig',
                      'CDEGGwen', 'Harley', 'Hastings', 'Hazel', 'Heather', 'Helton', 'Henrietta', 'Heston',
                      'Holly', 'Hulda', 'Increase', 'India', 'Irene', 'Jackie', 'Jade', 'January', 'Jemma',
                      'Jenny', 'JeraldJerroldJerry', 'Jessie', 'JethroJigar', 'JillJocelynJodieJoey',
                      'JustineKate', 'KathrynKeaton', 'KendraHIJKKerr', 'Kimball', 'Kitty', 'KristyKylie',
                      'LarenLawrence', 'Lawson', 'LeanneLianneLouise', 'LuciMaddox', 'MalfordMarlene',
                      'MaudMelindaMelville', 'MindyMolly', 'Mort', 'Nancy', 'Nelson', 'NigelOsbertOttiliePamela',
                      'PascoePercyPiper', 'LMNOPPippa', 'Poppy', 'Raleigh', 'Rebecca', 'ReynoldRhoda', 'Riley',
                      'Roland', 'RosaleenRosalie', 'Rosie', 'Ruby', 'Rupert', 'Ruth', 'Savannah', 'Scarlett',
                      'SharonSheridan', 'Shiloh', 'Sidney', 'Stacy', 'Sue', 'Sydney', 'Tammy', 'Tim',
                      'TimmyTimothy', 'Tracy', 'Travis', 'Trent', 'TrudieTucker', 'VelmaVicaryRSTVViolet',
                      'Walker', 'Warren', 'Whitney', 'WilfriedWoodrow']

pokemon_list = {
    "Bulbasaur":{
        "id":1,
        "type":[Types.GRASS, Types.POISON],
        "stats":Stats(45, 49, 49, 65, 65, 45)
    },
    "Pikachu":{
        "id":25,
        "type":[Types.ELECTRIC],
        "stats":Stats(35, 55, 30, 50, 40, 90)
    },
    "Magneton":{
        "id":82,
        "type":[Types.ELECTRIC, Types.STEEL],
        "stats":Stats(50, 60, 95, 120, 70, 70)
    },
    "Eevee":{
        "id":133,
        "type":[Types.NORMAL],
        "stats":Stats(55, 55, 50, 45, 65, 55)
    },
    "Vaporeon":{
        "id":134,
        "type":[Types.WATER],
        "stats":Stats(130, 65, 60, 110, 95, 65)
    },
    "Dragonair":{
        "id":148,
        "type":[Types.DRAGON],
        "stats":Stats(61, 84, 65, 70, 70, 70)
    },
    "Mareep":{
        "id":179,
        "type":[Types.ELECTRIC],
        "status":Stats(55, 40, 40, 65, 45, 35)
    },
    "Wobbuffet":{
        "id":202,
        "type":[Types.PSYCHIC],
        "stats":Stats(190, 33, 58, 33, 58, 33)
    }
}