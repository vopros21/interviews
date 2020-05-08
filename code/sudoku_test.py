import unittest
from code.sudoku import intersection


class SudokuIntersectionsTest(unittest.TestCase):

    def test_intersections(self):
        set_1 = set(range(5))
        set_2 = set(range(4))
        set_3 = set(range(3, 7))
        result = intersection(set_1, set_2, set_3)
        self.assertEqual(result, {3, })
