def even_parameters(func):
    def wrapper(*args):
        for el in args:
            try:
                if el % 2 != 0:
                    return "Please use only even numbers!"
            except:
                return "Please use only even numbers!"

        return func(*args)
    return wrapper
#
#
# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))

import unittest


class EvenParametersTests(unittest.TestCase):
    def test_even(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 4, 4)
        self.assertEqual(result, 12)

    def test_odd(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 5, 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_non_integer_params(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, "4", 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_no_params(self):
        @even_parameters
        def func():
            return "hi"

        result = func()
        self.assertEqual(result, "hi")


if __name__ == '__main__':
    unittest.main()
