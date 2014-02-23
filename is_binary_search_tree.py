#!/usr/bin/env python

import unittest

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def extrema_of_binary_search_tree(t, minimum=False):
    """
    Return the extrema of the binary tree rooted at t.
    None is returned if it is not a binary tree.
    """
    if t == None:
        return True
    extreme_val = t.val
    if t.left != None:
        left = extrema_of_binary_search_tree(t.left)
        if left == None or left >= t.val:
            return None
    if t.right != None:
        right = extrema_of_binary_search_tree(t.right)
        if right == None or t.val <= right:
            return None
    return extreme_val

def is_binary_search_tree(t):
    """
    Return True if tree rooted at t is a binary tree.
    """
    return extrema_of_binary_search_tree(t) != None


class TestBinaryTree(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_binary_search_tree(None))

    def test_one(self):
        self.assertTrue(is_binary_search_tree(TreeNode(-1)))

    def test_twotree(self):
        self.assertTrue(is_binary_search_tree(TreeNode(-1, TreeNode(-5), TreeNode(8))))

    def test_twotree(self):
        self.assertFalse(is_binary_search_tree(TreeNode(6, TreeNode(4), TreeNode(4))))


if __name__ == "__main__":
    unittest.main()
