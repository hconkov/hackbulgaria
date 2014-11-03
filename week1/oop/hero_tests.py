import unittest

from hero import Hero
from weapon import Weapon


class TestHero(unittest.TestCase):

    def test_hero_constructor(self):
        new_hero = Hero("Ico", 100, "old man")
        self.assertEqual(new_hero.name, "Ico")
        self.assertEqual(new_hero.health, 100)
        self.assertEqual(new_hero.nickname, "old man")

    def test_is_alive_when_dead(self):
        new_hero = Hero("Ico", 100, "old man")
        new_hero.health = 0
        self.assertFalse(new_hero.is_alive())

    def test_is_alive_when_isalive(self):
        new_hero = Hero("Ico", 100, "old man")
        self.assertTrue(new_hero.is_alive())

    def test_known_as(self):
        new_hero = Hero("Ico", 100, "old man")
        self.assertEqual(new_hero.known_as(), 'Ico the old man')

    def test_get_health(self):
        new_hero = Hero("Ico", 100, "old man")
        self.assertEqual(new_hero.get_health(), 100)

    def test_take_damage_int(self):
        new_hero = Hero("Ico", 100, "old man")
        new_hero.take_damage(20)
        self.assertEqual(new_hero.get_health(), 80)

    def test_take_damage_float(self):
        new_hero = Hero("Ico", 100, "old man")
        new_hero.take_damage(19.5)
        self.assertEqual(new_hero.get_health(), 80.5)

    def test_take_damage_more_then_hp(self):
        new_hero = Hero("Ico", 100, "old man")
        new_hero.take_damage(101)
        self.assertEqual(new_hero.get_health(), 0)

    def test_take_healing(self):
        new_hero = Hero("Ico", 100, "old man")
        new_hero.health = 20
        healing_result = new_hero.take_healing(20)
        self.assertEqual(new_hero.get_health(), 40)
        self.assertTrue(healing_result)

    def test_take_healing_dead(self):
        new_hero = Hero("Ico", 100, "old man")
        new_hero.health = 0
        healing_result = new_hero.take_healing(20)
        self.assertEqual(new_hero.get_health(), 0)
        self.assertFalse(healing_result)

    def test_take_healing_over_healing(self):
        new_hero = Hero("Ico", 120, "old man")
        new_hero.health = 110
        healing_result = new_hero.take_healing(40)
        self.assertEqual(new_hero.get_health(), 120)
        self.assertTrue(healing_result)

    def test_has_weapon_and_equip_weapon(self):
        new_hero = Hero("Ico", 100, "old man")
        new_weapon = Weapon("Axe", 25, 0.2)
        self.assertFalse(new_hero.has_weapon())
        new_hero.equip_weapon(new_weapon)
        self.assertTrue(new_hero.has_weapon())

    def test_attack(self):
        new_hero = Hero("Ico", 100, "old man")
        new_weapon = Weapon("Axe", 25, 0.2)
        self.assertFalse(new_hero.has_weapon())
        self.assertEqual(new_hero.attack(), 0)
        new_hero.equip_weapon(new_weapon)
        self.assertTrue(new_hero.has_weapon())
        self.assertEqual(new_hero.attack(), 25)

if __name__ == '__main__':
    unittest.main()
