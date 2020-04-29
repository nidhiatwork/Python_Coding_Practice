# Determine whether or not a linked list is a palindrome.

import unittest
class Node():
  def __init__(self, val, next=None):
    self.val, self.next = val, next

  def __str__(self):
    string = str(self.val)
    if self.next:
      string += ',' + str(self.next)
    return string
    
def is_palindrome_1(head):
    forward_head = head
    backward_head = None
    while head:
        n = Node(head.val)
        n.next = backward_head
        backward_head = n
        head = head.next
    
    while forward_head:
        if forward_head.val!=backward_head.val:
            return False
        forward_head, backward_head = forward_head.next, backward_head.next
    return True

def is_palindrome_2(head):
  forward, backward = head, copy_reverse(head)
  while forward:
    if forward.val != backward.val:
      return False
    forward, backward = forward.next, backward.next
  return True

def copy_reverse(head):
  prev = None
  node = copy(head)
  while node:
    next = node.next
    node.next = prev
    prev = node
    node = copy(next)
  return prev

def copy(node):
  if node:
    return Node(node.val, node.next)
  else:
    return None


class Test(unittest.TestCase):
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome_1(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome_1(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome_1(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome_1(list4))
    
  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(copy_reverse(head)), "40,30,20,10")

if __name__ == "__main__":
  unittest.main()

