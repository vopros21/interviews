import unittest
import mysort.quick_sort_hoare as h_sort


class TestSmallList(unittest.TestCase):
    def test_different_values(self):
        """Test short list with different values"""
        sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        short_different = [1, 0, 3, 6, 5, 9, 4, 2, 8, 7]
        h_sort.hoare_sort(short_different)
        self.assertEqual(sample, short_different, "Sorting result is inappropriate")
