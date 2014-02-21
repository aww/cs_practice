#!/usr/bin/env python

import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def revList(self, head):
        prev = None
        next = head
        while (next):
            tmp = next.next
            next.next = prev
            prev = next
            next = tmp
        return prev
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        newhead = self.revList(head)
        self.revList(newhead)
        return head == newhead


class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertFalse(self.sol.hasCycle(None))

    def test_one(self):
        self.assertFalse(self.sol.hasCycle(ListNode(1)))

    def test_onecycle(self):
        l = ListNode(1)
        l.next = l
        self.assertTrue(self.sol.hasCycle(l))

    def test_two(self):
        self.assertFalse(self.sol.hasCycle(ListNode(1, ListNode(2))))

    def test_twocycle(self):
        l = ListNode(1, ListNode(2))
        l.next.next = l
        self.assertTrue(self.sol.hasCycle(l))

    def test_three(self):
        self.assertFalse(self.sol.hasCycle(ListNode(1, ListNode(2, ListNode(3)))))

    def test_threecycle(self):
        l = ListNode(1, ListNode(2, ListNode(3)))
        l.next.next.next = l.next
        self.assertTrue(self.sol.hasCycle(l))

if __name__ == "__main__":
    unittest.main()
