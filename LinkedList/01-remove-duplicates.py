#Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

import unittest

def remove_duplicates(head):
  runner = head
  seen = {runner.data}
  if runner:
      while runner.next:
        if runner.next.data in seen:
          runner.next = runner.next.next
        else:
          seen.add(runner.next.data)
          runner = runner.next
  return head

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
  unittest.main()

