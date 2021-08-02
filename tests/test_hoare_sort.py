import unittest
import random

import mysort.quick_sort_hoare as h_sort
import mysort.merge_sort as m_sort


class TestSmallList(unittest.TestCase):
    def test_different_values(self):
        """Test short list with different values"""
        sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        short_different = random.sample(range(10), 10)
        h_sort.hoare_sort(short_different)
        self.assertEqual(sample, short_different, "Sorting result hoare_sort is inappropriate")
        short_different = random.sample(range(10), 10)
        m_sort.merge_sort(short_different)
        self.assertEqual(sample, short_different, 'Sorting result from merge_sort is inappropriate')

    def test_repeated_values(self):
        """Test a list with repeated values"""
        sample = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        short_repeated = random.sample(range(10), 10) + random.sample(range(10), 10)
        h_sort.hoare_sort(short_repeated)
        self.assertEqual(sample, short_repeated, "Sorting result hoare_sort is inappropriate")
        short_repeated = random.sample(range(10), 10) + random.sample(range(10), 10)
        m_sort.merge_sort(short_repeated)
        self.assertEqual(sample, short_repeated, 'Sorting result from merge_sort is inappropriate')

    def test_same_values(self):
        """Test list with the same values"""
        sample = [1, 1, 1, 1, 1, 1, 1]
        short_same = [1, 1, 1, 1, 1, 1, 1]
        h_sort.hoare_sort(short_same)
        self.assertEqual(sample, short_same, "Sorting result from hoare_sort is strange")
        m_sort.merge_sort(short_same)
        self.assertEqual(sample, short_same, "Sorting result from merge_sort is strange")

    def test_empty_list(self):
        """Test sorting for empty list"""
        sample = []
        empty_list = []
        h_sort.hoare_sort(empty_list)
        self.assertEqual(sample, empty_list, "Sorting result from hoare_sort is strange")
        m_sort.merge_sort(empty_list)
        self.assertEqual(sample, empty_list, "Sorting result from merge_sort is strange")
