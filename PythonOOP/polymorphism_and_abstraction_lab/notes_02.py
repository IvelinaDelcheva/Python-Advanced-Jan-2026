# Abstraction
from abc import ABC, abstractmethod


# for a class to be abstract we must inherit ABC class
# and to have at least one abstract method
# when we have abstract method we should override it in the child classes
# otherwise we will not be able to make an instance for the child class
# this in python enforces polymorphism
#  we also cannot create instance of the abstract class
# if we remove the abstract method we will be able to create an instance
# but this will not be abstract class anymore
# we need at least 1 abstract method and to inherit the ABC class
# to call a class abstract
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def greet(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError('name must be at least 2 characters')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('age must be positive')
        self.__age = value


class Player(Person):
    def greet(self):
        return f'Hi, I am a player {self.name}'


class Teacher(Person):
    def greet(self):
        return f'Hi, I am a teacher {self.name}'


for obj in [Teacher('Tname', 50), Player('Pname', 30)]:
    print(obj.greet())
