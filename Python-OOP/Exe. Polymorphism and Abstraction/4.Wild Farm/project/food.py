from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity


class Meat(Food):
    pass

class Vegetable(Food):
    pass

class Fruit(Food):
    pass

class Seed(Food):
    pass