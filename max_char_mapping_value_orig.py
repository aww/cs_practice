example_string = "Aaa bCc."
example_string2 = "Molly's sister's boyfriend's dog's name is Roger."


def max_value(string):
  """
You are given a list of strings (optionally as an input file). The value of given string is the sum of the values of all of its characters. For each string, the goal is to compute the maximum possible "value" by optimizing the one-to-one mapping of letters to the number range [1,26]. The case of a letter does not affect its value; spaces and punctuation have no value.

Input: String
Output: Value of string
"""
  count_chars = {}
  string = string.lower()
  for c in string:
    if c not in 'abcdefghijklmnopqrstuvwxyz':
      continue
    if c in count_chars:
      count_chars[c]+=1
    else:
      count_chars[c]=1
  # count_chars
  
  sorted_tuples = sorted(count_chars.items(), key=lambda x: x[1], reverse=True)
  #example_sorted_tuples = [('a', 3), ('c', 2), ('b', 1)]
  # map max -> 26, next -> 25
  char_values = {}
  for i, tuple in enumerate(sorted_tuples):
    char_values[tuple[0]] = 26-i
  
  # loop over string and find sum
  sum = 0
  for c in string:
    if c not in 'abcdefghijklmnopqrstuvwxyz':
      continue
    sum += char_values[c]
    
  return sum
  

print max_value(example_string)
print max_value(example_string2)
