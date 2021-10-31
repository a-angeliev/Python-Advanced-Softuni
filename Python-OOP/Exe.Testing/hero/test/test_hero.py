from unittest import TestCase, main
from project.hero import Hero

class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Nasko", 80, 2000, 300)
        self.enemy_hero = Hero("pesho", 10, 200, 50)

    def test_obj_init(self):
        self.assertEqual("Nasko", self.hero.username)
        self.assertEqual(80, self.hero.level)
        self.assertEqual(2000, self.hero.health)
        self.assertEqual(300, self.hero.damage)

    def test_fight_yourself_exception_raise(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_fight_with_low_hp_exception_raise(self):
        hero = Hero("Nasko", 80, -10, 300)
        with self.assertRaises(ValueError) as ex:
            hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fight_with_enemy_low_hp_exepction_raise(self):
        enemy_hero = Hero("pesho", 10, -50, 50)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight pesho. He needs to rest", str(ex.exception))

    def test_fight_with_both_dead_return(self):
        hero = Hero("Nasko", 80, 2000, 300)
        enemy_hero = Hero("pesho", 80, 2000, 300)

        a = hero.battle(enemy_hero)
        self.assertEqual("Draw", a)

    def test_fight_with_enemy_dead_return(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(81, self.hero.level)
        self.assertEqual(1505, self.hero.health)
        self.assertEqual(305, self.hero.damage)
        self.assertEqual("You win", result)

    def test_fight_with_you_dead_return(self):
        result = self.enemy_hero.battle(self.hero)
        self.assertEqual(81, self.hero.level)
        self.assertEqual(1505, self.hero.health)
        self.assertEqual(305, self.hero.damage)
        self.assertEqual("You lose", result)

    def test_string_representation(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n", str(self.hero))

if __name__ == "__main__":
    main()
