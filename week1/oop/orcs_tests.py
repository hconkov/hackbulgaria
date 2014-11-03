import unittest

from orcs import Orc


class TestOrc(unittest.TestCase):

    def test_orc_constructor(self):
        new_orc = Orc("Ico", 100, 1.5)
        self.assertEqual(new_orc.name, "Ico")
        self.assertEqual(new_orc.health, 100)
        self.assertEqual(new_orc.berserk_factor, 1.5)

    def test_is_alive_when_dead(self):
        new_orc = Orc("Ico", 100, 1.5)
        new_orc.health = 0
        self.assertFalse(new_orc.is_alive())

    def test_is_alive_when_isalive(self):
        new_orc = Orc("Ico", 100, 1.5)
        self.assertTrue(new_orc.is_alive())

    def test_get_health(self):
        new_orc = Orc("Ico", 100, 1.5)
        self.assertEqual(new_orc.get_health(), 100)

    def test_take_damage_int(self):
        new_orc = Orc("Ico", 100, 1.5)
        new_orc.take_damage(20)
        self.assertEqual(new_orc.get_health(), 80)

    def test_take_damage_float(self):
        new_orc = Orc("Ico", 100, 1.5)
        new_orc.take_damage(19.5)
        self.assertEqual(new_orc.get_health(), 80.5)

    def test_take_damage_more_then_hp(self):
        new_orc = Orc("Ico", 100, 1.5)
        new_orc.take_damage(101)
        self.assertEqual(new_orc.get_health(), 0)

    def test_take_healing(self):
        new_orc = Orc("Ico", 100, 1.5)
        new_orc.health = 20
        healing_result = new_orc.take_healing(20)
        self.assertEqual(new_orc.get_health(), 40)
        self.assertTrue(healing_result)

    def test_take_healing_dead(self):
        new_orc = Orc("Ico", 100, 1.5)
        new_orc.health = 0
        healing_result = new_orc.take_healing(20)
        self.assertEqual(new_orc.get_health(), 0)
        self.assertFalse(healing_result)

    def test_take_healing_over_healing(self):
        new_orc = Orc("Ico", 120, 1.5)
        new_orc.health = 110
        healing_result = new_orc.take_healing(40)
        self.assertEqual(new_orc.get_health(), 120)
        self.assertTrue(healing_result)

    def test_berserk_factor(self):
        new_orc = Orc("Ico", 100, 2.5)
        new_orc.fix_berserk_factor()
        self.assertEqual(new_orc.berserk_factor, 2)
        new_orc.berserk_factor = 0.5
        new_orc.fix_berserk_factor()
        self.assertEqual(new_orc.berserk_factor, 1)

if __name__ == '__main__':
    unittest.main()
