# Implement a stack with a function that returns the current minimum item.

class MinStack():
  def __init__(self):
    self.top, self.min = None, None
    
  def mininum(self):
    if not self.min:
      return None
    return self.min.data
    
  def push(self, item):
    if self.min and (self.min.data < item):
      self.min = Node(data=self.min.data, next=self.min)
    else:
      self.min = Node(data=item, next=self.min)
    self.top = Node(data=item, next=self.top)
  
  def pop(self):
    if not self.top:
      return None
    self.min = self.min.next
    item = self.top.data
    self.top = self.top.next
    return item

class Node():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

import unittest

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = MinStack()
    self.assertEqual(min_stack.mininum(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.mininum(), 7)
    min_stack.push(6)
    min_stack.push(5)
    self.assertEqual(min_stack.mininum(), 5)
    min_stack.push(10)
    self.assertEqual(min_stack.mininum(), 5)
    self.assertEqual(min_stack.pop(), 10)
    self.assertEqual(min_stack.pop(), 5)
    self.assertEqual(min_stack.mininum(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.mininum(), None)

if __name__ == "__main__":
  unittest.main()

