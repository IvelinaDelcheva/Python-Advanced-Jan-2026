from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    @property
    def animal_sound(self):
        return "Squeak"

    @property
    def weight_increase(self):
        return 0.10

    @property
    def food_allowed(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    @property
    def animal_sound(self):
        return "Woof!"

    @property
    def weight_increase(self):
        return 0.40

    @property
    def food_allowed(self):
        return [Meat]


class Cat(Mammal):
    @property
    def animal_sound(self):
        return "Meow"

    @property
    def weight_increase(self):
        return 0.30

    @property
    def food_allowed(self):
        return [Vegetable, Meat]


class Tiger(Mammal):
    @property
    def animal_sound(self):
        return "ROAR!!!"

    @property
    def weight_increase(self):
        return 1.00

    @property
    def food_allowed(self):
        return [Meat]
