from orc import Orc
from hero import Hero
from random import *


class Fight:

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc
        self.first_attacker = 0
        self.second_attacker = 0

    def coin_flip(self):
        if random.choice([True, False]) is True:
            print("The hero attacks first!")
            print()
            return True
        else:
            print("The orc attacks first!")
            print()
            return False

    def simulate_fight(self):
        while self.hero.is_alive() is True and self.orc.is_alive() is True:
            if self.coin_flip() is True:
                self.hero_attack()
                if self.orc.is_alive is True:
                    self.orc_attack()
            else:
                self.orc_attack()
                if self.hero.is_alive() is True:
                    self.hero_attack()
        if self.hero.is_alive is True:
            return("{} won the fight!".format(self.hero.known_as()))
        else:
            return("The orc has won and {} perished.".format(self.hero.known_as()))

    def hero_attack(self):
        damage = self.hero.attack()
        print("Your hero dealt {} damage".format(damage))
        self.orc.take_damage(damage)
        print("Orc has {} health".format(self.orc.get_health()))
        print()

    def orc_attack(self):
        damage = self.orc.attack()
        print("The orc dealt {} damage".format(damage))
        self.hero.take_damage(damage)
        print("Hero's helth is {}".format(self.hero.get_health()))
        print()
