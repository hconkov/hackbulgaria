from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        self.berserk_factor = berserk_factor
        super().__init__(name, health)

    def fix_berserk_factor(self):
        if self.berserk_factor > 2.0:
            self.berserk_factor = 2.0
        elif self.berserk_factor < 1.0:
            self.berserk_factor = 1.0
