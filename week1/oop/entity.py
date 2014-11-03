from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = False

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health = self.health - damage_points

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points > self.max_health:
            self.health = self.max_health
            return True
        else:
            self.health = self.health + healing_points
            return True

    def has_weapon(self):
        if self.weapon is False:
            return False
        else:
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.has_weapon() is False:
            return 0
        else:
            return self.weapon.damage
