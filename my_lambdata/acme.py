
import unittest
from random import randint, sample, uniform


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        steal = self.price/self.weight
        if steal < 0.5:
            return "Not so stealable"
        elif steal < 1:
            return "Kinda stealable"
        else:
            return "Very stealable"

    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            return "fizzle"
        elif explode < 50:
            return "boom"
        else:
            return "BABOOM"


class BoxingGlove(Product):
    def __init__(self, name, price=10, flammability=0.5, weight=10):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "it's a glove"

    def punch(self):
        if weight < 5:
            return "That tickles"
        elif weight < 15:
            return "Hey that hurt"
        else:
            return "OUCH"


        





