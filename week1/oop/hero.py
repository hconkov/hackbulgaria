class Hero:

    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
        self.max_health = health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def known_as(self):
        return('%s the %s' % (self.name, self.nickname))

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
