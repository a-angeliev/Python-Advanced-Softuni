def shopping_list(money, **kwargs):
    products = {}
    if money < 100:
        return "You do not have enough budget."

    for key, value in kwargs.items():
        if len(products) == 5:
            break
        price = value[0]
        queantity = value[1]
        result = price * queantity
        if result < money:
            if not key in products:
                products[key] = result
            else:
                products[key] += result
            money -= result
            # del kwargs[key]
    # if not products:
    #     return
    # else:
    string = ""
    coutn = len(products)
    iters = 0
    for key, value in products.items():
        if iters != coutn - 1:
            string += f"You bought {key} for {value:.2f} leva.\n"
            iters +=1
        else:
            string += f"You bought {key} for {value:.2f} leva."
    return string


#
#
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, -5),
                    ))



# import unittest
#
# class Tests(unittest.TestCase):
#     def test(self):
#         result = shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     )
#         self.assertEqual(result.strip(), "You bought cola for 2.40 leva.\nYou bought candies for 3.75 leva.\nYou bought bread for 1.80 leva.\nYou bought pie for 52.50 leva.\nYou bought tomatoes for 4.20 leva.")
#
# if __name__ == "__main__":
#     unittest.main()