#!/usr/bin/env python

import unittest

class Solution:
    def __init__(self):
        self.twodig = set(map(lambda x: "%d" % x, range(10, 27)))
        self.onedig = set(map(lambda x: "%d" % x, range(1,10)))
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s)==0:
            return 0
        ndecodings = []
        for i in range(len(s)):
            if i == 0:
                if s[i] in self.onedig:
                    ndecodings.append(1)
                else:
                    return 0
            else:
                decodings = 0
                if s[i-1:i+1] in self.twodig:
                    decodings += ndecodings[i-2]
                if s[i] in self.onedig:
                    decodings += ndecodings[i-1]
                if decodings == 0:
                    return 0
                ndecodings.append(decodings)
        return ndecodings[-1]

class TestNumDecodings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def test_example(self):
        self.assertEqual(self.sol.numDecodings("12"), 2)
    def test_empty(self):
        self.assertEqual(self.sol.numDecodings(""), 0)
    def test_zeroprefix(self):
        self.assertEqual(self.sol.numDecodings("012"), 0)
    def test_nondigit(self):
        self.assertEqual(self.sol.numDecodings("XX"), 0)
    def test_mytest(self):
        self.assertEqual(self.sol.numDecodings("1234567891011"), 6)
        #"1 2 3 4 5 6 7 8 9 10 11"
        #"1 2 3 4 5 6 7 8 9 10 1 1"
        #"1 23 4 5 6 7 8 9 10 11"
        #"1 23 4 5 6 7 8 9 10 1 1"
        #"12 3 4 5 6 7 8 9 10 11"
        #"12 3 4 5 6 7 8 9 10 1 1"

if __name__ == "__main__":
    unittest.main()
