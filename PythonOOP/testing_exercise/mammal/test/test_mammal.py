from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal('Mammal Name', 'Cat', 'Meow')

    def test_init(self):
        self.assertEqual('Mammal Name', self.mammal.name)
        self.assertEqual('Cat', self.mammal.type)
        self.assertEqual('Meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()
