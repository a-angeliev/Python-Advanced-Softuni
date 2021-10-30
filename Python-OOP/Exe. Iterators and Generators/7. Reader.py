def read_next(*args):
    for el in args:
        for el in el:
            yield el


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        res = ''
        for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
            res += str(item)
        self.assertEqual(res, 'string2dict')

if __name__ == '__main__':
    unittest.main()