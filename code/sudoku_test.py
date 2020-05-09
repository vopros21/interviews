import unittest
from code.sudoku import intersection


class SudokuIntersectionsTest(unittest.TestCase):

    def test_intersections(self):
        set_1, set_2, set_3 = {1, 2, 3, 7, 9}, {1, 3, 6, 7}, {2, 4, 7}
        result = intersection(set_1, set_2, set_3)
        self.assertEqual({5, 8}, result)
        set_1, set_2, set_3 = set_2, set_3, {1, 2, 3}
        result = intersection(set_1, set_2, set_3)
        self.assertEqual({5, 8, 9}, result)


