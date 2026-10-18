from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def animal_sound(self):
        return "Hoot Hoot"

    @property
    def weight_increase(self):
        return 0.25

    @property
    def food_allowed(self):
        return [Meat]


class Hen(Bird):

    @property
    def animal_sound(self):
        return "Cluck"

    @property
    def weight_increase(self):
        return 0.35

    @property
    def food_allowed(self):
        return [Vegetable, Fruit, Meat, Seed]

