#!/usr/bin/env python

import unittest

def selection_sort(list):
    """Sort list in place using bubble sort"""
    N = len(list)
    for i in xrange(N):
        # list[i:] is sorted
        iSmall = i
        for j in xrange(iSmall+1, N):
            if list[j] < list[iSmall]:
                iSmall = j
        if iSmall != i:
            # swap i and iSmall
            tmp = list[i]
            list[i] = list[iSmall]
            list[iSmall] = tmp


class TestSelectionSort(unittest.TestCase):
    def test_empty(self):
        l = []
        selection_sort(l)
        self.assertEqual(l, [])

    def test_one(self):
        l = [1,2]
        selection_sort(l)
        self.assertEqual(l, [1,2])

    def test_onerev(self):
        l = [2,1]
        selection_sort(l)
        self.assertEqual(l, [1,2])

    def test_many(self):
        l = [-3, 4, 5, 1.9, 1, 8, 324, -3, 43]
        lsort = sorted(l)
        selection_sort(l)
        self.assertEqual(l, lsort)

if __name__ == "__main__":
    unittest.main()
