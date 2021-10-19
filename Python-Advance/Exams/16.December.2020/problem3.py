def get_magic_triangle(n):
    start = [[1], [1, 1]]
    row = 2
    for new_line in range(n-2):
        start.append([])
        for index in range(new_line + 3):
            if index == 0:
                start[row].append(1)
            elif index == new_line + 2:
                start[row].append(1)
            else:
                start[row].append(start[row -1][index-1] + start[row -1][index])
        row += 1
    return start
get_magic_triangle(5)


import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()