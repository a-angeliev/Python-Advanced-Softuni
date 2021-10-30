from project.animals.animal import Bird
from project.food import *

class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self,food):
        if food.__class__.__name__ == "Meat":
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity


# a = Owl("gosho", 1 , 1)
# print(a)
# b = Meat(4)
# c = Seed(1)
# a.feed(b)
# print(a)
# # a.feed(c)