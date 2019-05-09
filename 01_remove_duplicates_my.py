"""
#Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

"""
import unittest
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(head):
    dummy = head
    vals = set()
    prev = head
    while head:
        if head.val in vals:
            prev.next = head.next
        else:
            vals.add(head.val)
            prev = head
        head = head.next
    return dummy

class Test (unittest.TestCase):
    def test_operate(self):
        n = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
        head = operate(n)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 3)
        self.assertEqual(head.next.next.val, 5)

if __name__=="__main__":
    unittest.main()