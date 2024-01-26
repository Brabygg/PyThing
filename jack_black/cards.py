from enum import Enum

class suit(Enum):
    Diamonds = "D"
    Hearts = "H"
    Spades = "S"
    Clubs = "C"

class type(Enum):
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eight = "8"
    Nine = "9"
    Ten = "10"
    Jack = "11"
    Queen = "12"
    King = "13"
    Ace = "-1"

class card:
    def __init__(self, suit, type):
        self.suit = suit
        self.type = type
        self.value = int(type.value)
        if int(self.value) > 10:
            self.value = 10

def reshuffle():
    deck = []
    for suit_data in suit:
        for type_data in type:
            new_card = card(suit_data, type_data)
            deck.append(new_card)

    return deck