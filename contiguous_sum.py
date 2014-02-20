#!/usr/bin/env python

import unittest

def contiguous_sum(list):
    """Return the largest sum from any non-contiguous subset of 'list'.
    
    I will assume you can pick none and this has sum 0, so []->0 or [-1,-2,-3]->0
    'list' must be iterable and full of objects that can be summed, ordered, and compared to 0."""
    best_sums = []
    if len(list) < 1: # hopefully this will raise an exception if we can't iterate on the object
        return 0
    for i in range(len(list)):
        if i==0:
            best_sums.append(max(list[i], 0))
        elif i==1:
            best_sums.append(max(list[i], list[i-1], 0))
        else:
            best_sums.append(max(best_sums[i-1], best_sums[i-2], best_sums[i-2]+list[i], 0))
    return best_sums[-1]

class ContiguousSumTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(contiguous_sum([]),
                         0)

    def test_one(self):
        self.assertEqual(contiguous_sum([5]),
                         5)

    def test_oneneg(self):
        self.assertEqual(contiguous_sum([-88]),
                         0)

    def test_two(self):
        self.assertEqual(contiguous_sum([2, 3]),
                         3)

    def test_manyneg(self):
        self.assertEqual(contiguous_sum([-5, -8, -10]),
                         0)

    def test_consecutive(self):
        self.assertEqual(contiguous_sum([1, 2, 3, 4, 5, 6, 7, 8]),
                         2+4+6+8)

    def test_random(self):
        self.assertEqual(contiguous_sum([-3, 4, 1, 1, 8, 2, -3, 20]),
                         4+8+20) # I think this is correct


if __name__ == "__main__":
    unittest.main()
