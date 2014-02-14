#!/usr/bin/env python

import unittest

words = set(["dog", "clog", "cat", "mouse", "rat", "can",
             "fig", "dig", "mud", "a", "an", "duh", "sin",
             "get", "shit", "done", "all", "glory", "comes",
             "from", "daring", "to", "begin", ])

dialmap = {
    'a':2, 'b':2, 'c':2,
    'd':3, 'e':3, 'f':3,
    'g':4, 'h':4, 'i':4,
    'j':5, 'k':5, 'l':5,
    'm':6, 'n':6, 'o':6,
    'p':7, 'q':7, 'r':7, 's':7,
    't':8, 'u':8, 'v':8,
    'w':9, 'x':9, 'y':9, 'z':9,
    }

def tonumbers(word):
    """Convert the string 'word' into the equivalent string of phone-dailing numbers"""
    numstr = ''
    for c in word.lower():
        numstr += str(dialmap[c])
    return numstr
    
wordsnum = set()
for w in words:
    wordsnum.add(tonumbers(w))

def isword(number):
    """Return True if the string of decimal digits 'number' can be represented
    as the concatenation of words in the 'words' set, otherwise False."""
    if number in wordsnum:
        return True
    if number in isword.memoized:
        return isword.memoized[number]
    for i in range(1, len(number)):
        a = number[i:]
        b = number[:i]
        #print locals()
        if isword(a) and isword(b):
            isword.memoized[number] = True
            return True
    isword.memoized[number] = False
    return False
isword.memoized = {}


class TestIsWord(unittest.TestCase):
    def testGetShitDone(self):
        self.assertTrue(isword(tonumbers('getshitdone')))
    def testHas1(self):
        self.assertFalse(isword('1092340345'))
    def testDogDog(self):
        self.assertTrue(isword(tonumbers('dogdog')))
    def testMyNumber1(self):
        self.assertFalse(isword('7342393309'))
    def testMyNumber2(self):
        self.assertFalse(isword('4082434090'))

if __name__ == "__main__":
    unittest.main()
