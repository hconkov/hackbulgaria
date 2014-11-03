import unittest

from weapon import Weapon


class TestWeapon(unittest.TestCase):

    def test_weapon_constructor(self):
        new_weapon = Weapon("Ico", 100, 0.2)
        self.assertEqual(new_weapon.name, "Ico")
        self.assertEqual(new_weapon.damage, 100)
        self.assertEqual(new_weapon.critical_strike_percent, 0.2)

    def test_weapon_critical(self):
        new_weapon = Weapon("Ico", 100, 0.2)
        self.assertEqual(new_weapon.name, "Ico")
        self.assertEqual(new_weapon.damage, 100)
        self.assertEqual(new_weapon.critical_strike_percent, 0.2)
        weapontests = []
        for n in range(1, 11):
            weapontests.append(new_weapon.critical_hit())
        self.assertIn(200, weapontests)
        self.assertIn(False, weapontests)


if __name__ == '__main__':
    unittest.main()
