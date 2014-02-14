#!/usr/bin/env python

import unittest

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

#9 4
#start=
def quicksort(a, start=0, end=-1):
    if end<0:
        end = len(a)
    if (end - start)  < 2:
        return
    # Pick a pivot and move it to the end for now
    iPivot = end-1
    if iPivot != end-1:
        swap(a, iPivot, end-1)
        iPivot = end-1
    j = start # index of first element of larger group
    for i in range(start, end-1):
        #print "In Loop:      ", locals() #a, "i=", i, "j=", j
        if a[i] < a[iPivot]:
            swap(a,i,j)
            j += 1
    swap(a,iPivot,j)
    #print "After Swap:   ", locals()
    quicksort(a, 0, j)
    quicksort(a, j+1, end)
    #print "End quicksort:", locals()

class TestQuicksort(unittest.TestCase):
    def testEmpty(self):
        test_data = []
        quicksort(test_data)
        self.assertEqual(test_data, [])

    def testOne(self):
        test_data = [3]
        quicksort(test_data)
        self.assertEqual(test_data, [3])

    def testTwoSame(self):
        test_data = [4, 4]
        quicksort(test_data)
        self.assertEqual(test_data, [4, 4])
    
    def testTwoDiffOrder(self):
        test_data = [4, 9]
        quicksort(test_data)
        self.assertEqual(test_data, [4, 9])

    def testTwoDiffRev(self):
        test_data = [9, 4]
        quicksort(test_data)
        self.assertEqual(test_data, [4, 9])

    def test123(self):
        test_data = [1, 2, 3]
        quicksort(test_data)
        self.assertEqual(test_data, [1, 2, 3])

    def test132(self):
        test_data = [1, 3, 2]
        quicksort(test_data)
        self.assertEqual(test_data, [1, 2, 3])

    def test312(self):
        test_data = [3, 1, 2]
        quicksort(test_data)
        self.assertEqual(test_data, [1, 2, 3])

    def test321(self):
        test_data = [3, 2, 1]
        quicksort(test_data)
        self.assertEqual(test_data, [1, 2, 3])

    def test213(self):
        test_data = [2, 1, 3]
        quicksort(test_data)
        self.assertEqual(test_data, [1, 2, 3])

    def test231(self):
        test_data = [2, 3, 1]
        quicksort(test_data)
        self.assertEqual(test_data, [1, 2, 3])

    def testComplexUnique(self):
        test_data = [5, 9, 2, 45, -23, 44, 92, 10003, 3, 4, 33, 22, ]
        quicksort(test_data)
        self.assertEqual(test_data, [-23, 2, 3, 4, 5, 9, 22, 33, 44, 45, 92, 10003, ])

    def testComplexDups(self):
        test_data = [5, 9, 2, 45, -23, -23, 92, 10003, 4, 4, 4, 22, ]
        quicksort(test_data)
        self.assertEqual(test_data, [-23, -23, 2, 4, 4, 4, 5, 9, 22, 45, 92, 10003, ])

if __name__ == "__main__":
    unittest.main()
