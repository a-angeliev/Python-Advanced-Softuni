from project.drink import Drink
from project.food import Food


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name):
        for el in self.products:
            if el.name == product_name:
                self.products.remove(el)
                break

    def __repr__(self):
        ret_into = ""
        for el in self.products:
            ret_into += f"{el.name}: {el.quantity}"
            if not el == self.products[-1]:
                ret_into += "\n"
        return ret_into
#
# salam = Food("salam")
# print(salam.quantity)
# salam.increase(10)
# print(salam.quantity)
# print(ProductRepository.products)