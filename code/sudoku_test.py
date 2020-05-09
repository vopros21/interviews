import unittest
import code.sudoku as su


class SudokuIntersectionsTest(unittest.TestCase):

    def test_intersections(self):
        set_1, set_2, set_3 = {1, 2, 3, 7, 9}, {1, 3, 6, 7}, {2, 4, 7}
        result = su.intersection(set_1, set_2, set_3)
        self.assertEqual({5, 8}, result)
        set_1, set_2, set_3 = set_2, set_3, {1, 2, 3}
        result = su.intersection(set_1, set_2, set_3)
        self.assertEqual({5, 8, 9}, result)

    def test_available_numbers(self):
        field = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]
        row = 0
        column = 1
        result = su.available_numbers(field, row, column)
        self.assertEqual({1, 9}, result)
        result = su.available_numbers(field, 1, 2)
        self.assertEqual({1, 4, 9}, result)

# class SudokuAvailableNumbersTest(unittest.TestCase):
#
#     def