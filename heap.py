#!/usr/bin/env python

import unittest

class heap:
    def __init__(self, array):
        """Save the array, we will modify it inplace"""
        self.a = array
        self.N = len(self.a)
        self.buildHeap()

    def swap(self, i, j):
        """Swap the values at index i and j in the interal array"""
        tmp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = tmp

    def buildHeap(self):
        """Build the internal array into a heap"""
        self.hs = self.N
        for i in range(self.hs/2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        """Assume the children of the element at i are valid max-heaps
        but the value at i may not be maximal and transform into a
        max-heap rooted at i"""
        iLeft = (i+1)*2 - 1
        iRight = (i+1)*2
        iLargest = i
        if iLeft < self.hs and self.a[iLeft] > self.a[i]:
            iLargest = iLeft
        if iRight < self.hs and self.a[iRight] > self.a[iLargest]:
            iLargest = iRight
        if iLargest != i:
            self.swap(iLargest, i)
            self.heapify(iLargest)

    def sort(self):
        for i in range(self.N-1, 0, -1):
            self.swap(0,i)
            self.hs = i
            self.heapify(0)



class TestHeap(unittest.TestCase):
    def testOne(self):
        h = heap([1])
        self.assertEqual(h.a[0], 1)
        h.sort()
        self.assertEqual(h.a, [1])

    def testTwoSame(self):
        h = heap([4, 4])
        self.assertEqual(h.a[0], 4)
        h.sort()
        self.assertEqual(h.a, [4,4])
    
    def testTwoDiff(self):
        h = heap([4, 9])
        self.assertEqual(h.a[0], 9)
        h.sort()
        self.assertEqual(h.a, [4,9])

    def testComplexUnique(self):
        h = heap([5, 9, 2, 45, -23, 44, 92, 10003, 3, 4, 33, 22, ])
        self.assertEqual(h.a[0], 10003)
        h.sort()
        self.assertEqual(h.a, [-23, 2, 3, 4, 5, 9, 22, 33, 44, 45, 92, 10003, ])

    def testComplexDups(self):
        h = heap([5, 9, 2, 45, -23, -23, 92, 10003, 4, 4, 4, 22, ])
        self.assertEqual(h.a[0], 10003)
        h.sort()
        self.assertEqual(h.a, [-23, -23, 2, 4, 4, 4, 5, 9, 22, 45, 92, 10003, ])

if __name__ == "__main__":
    unittest.main()
