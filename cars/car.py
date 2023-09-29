import itertools as it

class car:
    
    new_id = it.count()

    def __init__(self, brand, color, amount):
        self.id = self.new_id.__next__() + 1
        self.brand = brand
        self.color = color
        self.amount = amount