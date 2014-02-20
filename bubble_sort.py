#!/usr/bin/env python

import unittest

def bubble_sort(list):
    """Sort list in place using bubble sort"""
    N = len(list)
    for i in xrange(N, 0, -1):
        # list[i:] is sorted
        for j in xrange(i, N):
            if list[j] < list[j-1]:
                tmp = list[j-1]
                list[j-1] = list[j]
                list[j] = tmp


class TestBubble(unittest.TestCase):
    def test_empty(self):
        l = []
        bubble_sort(l)
        self.assertEqual(l, [])

    def test_one(self):
        l = [1,2]
        bubble_sort(l)
        self.assertEqual(l, [1,2])

    def test_onerev(self):
        l = [2,1]
        bubble_sort(l)
        self.assertEqual(l, [1,2])

    def test_many(self):
        l = [-3, 4, 5, 1.9, 1, 8, 324, -3, 43]
        lsort = sorted(l)
        bubble_sort(l)
        self.assertEqual(l, lsort)

if __name__ == "__main__":
    unittest.main()
