from entity import Entity


class Hero(Entity):

    def __init__(self, name, health, nickname):
        self.nickname = nickname
        super().__init__(name, health)

    def known_as(self):
        return('%s the %s' % (self.name, self.nickname))
