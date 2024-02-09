import things
import random as r

class room:
    def __init__(self, x, y, enemy, item):
        self.x = x
        self.y = y
        self.enemy = enemy
        self.item = item

def create_map(x, y, ec, ic):
    map = []

    xi = 0
    for column in range(x):
        yi = 0
        for row in range(y):
            new_enemy = None
            new_item = None
            if (r.randint(1, 100) <= ec):
                new_enemy = r.choice(things.enemies)
            if (r.randint(1, 100) <= ic):
                new_item = r.choice(things.items)
            map.append(room(xi, yi, new_enemy, new_item))
            yi += 1
        xi += 1
    
    return map