from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username: str = 'Hero1'
    health: float = 10.0
    damage: float = 1.0
    level: int = 5

    def setUp(self):
        self.hero1 = Hero(self.username, self.level, self.health, self.damage)
        self.hero2 = Hero('Hero2', self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero1.username)
        self.assertEqual(self.level, self.hero1.level)
        self.assertEqual(self.health, self.hero1.health)
        self.assertEqual(self.damage, self.hero1.damage)

    def test_battle_name_like_enemy_hero(self):
        self.hero2.username = 'Hero1'
        with self.assertRaises(Exception) as e:
            self.hero1.battle(self.hero2)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_battle_hero_health_0_or_less(self):
        self.hero1.health = 0
        with self.assertRaises(ValueError) as e:
            self.hero1.battle(self.hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

        self.hero1.health = -1
        with self.assertRaises(ValueError) as e:
            self.hero1.battle(self.hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_battle_enemy_hero_health_0_or_less(self):
        self.hero2.health = 0
        with self.assertRaises(ValueError) as e:
            self.hero1.battle(self.hero2)
        self.assertEqual(f"You cannot fight {self.hero2.username}. He needs to rest", str(e.exception))

        self.hero2.health = -1
        with self.assertRaises(ValueError) as e:
            self.hero1.battle(self.hero2)
        self.assertEqual(f"You cannot fight {self.hero2.username}. He needs to rest", str(e.exception))

    def test_draw(self):
        self.hero1.damage = 2
        self.hero2.damage = 2
        expected = self.hero1.battle(self.hero2)
        self.assertEqual("Draw", expected)

    def test_you_win(self):
        self.hero1.damage = 3
        self.hero1.level = 10

        expected = self.hero1.battle(self.hero2)
        self.assertEqual("You win", expected)
        self.assertEqual(11, self.hero1.level)
        self.assertEqual(10, self.hero1.health)
        self.assertEqual(8, self.hero1.damage)

    def test_you_lose(self):
        self.hero2.damage = 3
        self.hero2.level = 10

        expected = self.hero1.battle(self.hero2)
        self.assertEqual("You lose", expected)
        self.assertEqual(11, self.hero2.level)
        self.assertEqual(10, self.hero2.health)
        self.assertEqual(8, self.hero2.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        self.assertEqual(expected, str(self.hero1))


if __name__ == '__main__':
    main()
