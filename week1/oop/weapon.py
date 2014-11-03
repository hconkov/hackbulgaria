from random import *


class Weapon:

    def __init__(self, name, damage, critical_strike_percent):
        self.name = name
        self.damage = damage
        self.critical_hit = damage * 2
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        random = 0
        if random.choice[0.1, 1.0] < self.critical_strike_percent:
            return self.critical_hit
        else:
            return False
