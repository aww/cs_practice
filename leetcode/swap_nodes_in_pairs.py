#!/usr/bin/env python

import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def printList(node):
    if node:
        print node.val,
        printList(node.next)
        
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        newhead = head # covers the case 0 or 1 nodes
        previous = None
        current = head
        while (current and current.next):
            # going by ...->0->1->2->3 example where current is 1
            after = (current.next).next # store a link to 3
            (current.next).next = current # link 2->1  (->2...)
            first = current.next # store a link to 2
            current.next = after # link 1->3
            if previous:
                previous.next = first # link 0->2
            else:
                newhead = first
            previous = first.next # store a link to 1
            current = after
        return newhead

class TestSwapPairs(unittest.TestCase):
    def swapPairsAndList(self, head):
        sol = Solution()
        current = sol.swapPairs(head)
        # the rest just makes a list() out of the values from the linked list
        vallist = []
        while (current):
            vallist.append(current.val)
            current = current.next
        return vallist

    def test_empty(self):
        self.assertEqual(self.swapPairsAndList(None), [])

    def test_one(self):
        self.assertEqual(self.swapPairsAndList(ListNode(1)), [1])

    def test_two(self):
        head = ListNode(1, ListNode(2))
        self.assertEqual(self.swapPairsAndList(head), [2,1])

    def test_three(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual(self.swapPairsAndList(head), [2,1,3])

    def test_four(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(self.swapPairsAndList(head), [2,1,4,3])

if __name__ == "__main__":
    unittest.main()
