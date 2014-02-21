#!/usr/bin/env python

import unittest
import pprint
import collections

example_string = "Aaa bCc."
example_string2 = "Molly's sister's boyfriend's dog's name is Roger."


def max_value(string):
  """The value of given string is the sum of the values of all of its characters.
  For each string, the goal is to compute the maximum possible "value" by optimizing
  the one-to-one mapping of letters to the number range [1,26].
  The case of a letter does not affect its value; spaces and punctuation have no value.
  Input: String
  Output: Value of string
  """
  # Get the frequency of each character
  chars_to_count = 'abcdefghijklmnopqrstuvwxyz'
  count_chars = collections.defaultdict(int)
  string = string.lower()
  for c in string:
    if c in chars_to_count:
      count_chars[c] += 1
  
  sorted_char_frequency = sorted(count_chars.items(), key=lambda x: x[1], reverse=True)
  #example_sorted_tuples = [('a', 3), ('c', 2), ('b', 1)]
  # map max -> 26, next -> 25, etc.
  # we have the frequencies already, so compute the some of values as we go
  value = 0
  for i, char_freq in enumerate(sorted_char_frequency):
    value += (26-i)*char_freq[1]  
  return value

def value_of_strings(strings):
  return map(max_value, strings)
  
def valueNDiff(freq):
  """Given a list of character frequencies return the max_value where
  the most frequent character has value 26, second has value 25, etc.
  Input: list of non-negative integers
  Output: non-negative integer

  Used for testing max_value()."""
  sorted_freq = sorted(freq, reverse=True)
  return sum(map(lambda x: (26-x[0])*x[1], enumerate(sorted_freq)))

class TestMaxValue(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_value(example_string), valueNDiff([3,2,1]))
    def test_example2(self):
        self.assertEqual(max_value(example_string2), valueNDiff([1, 1, 2, 4, 1, 2, 3, 2, 2, 2, 4, 4, 7, 1, 2]))
    def test_singles(self):
        self.assertEqual(max_value("ABCd"), valueNDiff([1,1,1,1]))
    def test_junk(self):
        self.assertEqual(max_value("AaBb    @)#(*$)@(*%"), valueNDiff([2,2]))
    def test_empty(self):
        self.assertEqual(max_value(""), 0)

if __name__ == "__main__":
    unittest.main()
