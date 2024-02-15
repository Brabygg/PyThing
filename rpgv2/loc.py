import things
import random as r

class room:
    def __init__(self, x, y, enemy, item, wall):
        self.x = x
        self.y = y
        self.enemy = enemy
        self.item = item
        self.wall = wall
        self.visited = False
        self.seen = False

def create_map(x, y, ec, ic, wc):
    map = []

    xi = 0
    for column in range(x):
        yi = 0
        for row in range(y):
            new_enemy = None
            new_item = None
            has_wall = False

            if (r.randint(1, 100) <= ec):
                new_enemy = r.choice(things.enemies)
            if (r.randint(1, 100) <= ic):
                new_item = r.choice(things.items)
            if (r.randint(1, 100) <= wc):
                has_wall = True
            
            map.append(room(xi, yi, new_enemy, new_item, has_wall))
            yi += 1
        xi += 1
    
    return map