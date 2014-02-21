#!/usr/bin/env python

import unittest

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in '+-*/':
                b = int(stack.pop()) # exception here if not enough values or not int
                a = int(stack.pop())
                if token=='+':
                    result = a + b
                elif token=='-':
                    result = a - b
                elif token=='*':
                    result = a * b
                elif token=='/':
                    # we simulate C/C++ integer division, which is what leetcode wants, not floor division
                    result = abs(a) / abs(b)
                    if a*b < 0:
                        result = - result
                stack.append(result) # exception here if we don't catch the operator in the above switch
            else:
                stack.append(int(token)) # exception here if not an int
        return stack[0] # exception here if ran out of values


class TestRPN(unittest.TestCase, Solution):
    def test_example1(self):
        self.assertEqual(self.evalRPN(["2","1","+","3","*"]), 9)
    def test_example2(self):
        self.assertEqual(self.evalRPN(["4","13","5","/","+"]), 6)
    def test_complex(self):
        self.assertEqual(self.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)

if __name__ == "__main__":
    unittest.main()
