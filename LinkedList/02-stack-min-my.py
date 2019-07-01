"""
Implement a stack with a function that returns the current minimum item.
"""

class Node:
      def __init__(self, val, next=None):
            self.val = val
            self.next = next

class MinStack:
      def __init__(self):
            self.mins = None
            self.tops = None

      def push(self, item):
            if self.mins and item>self.mins.val:
                  self.mins = Node(val=self.mins.val, next=self.mins)
            else:
                  self.mins = Node(val=item, next=self.mins)
            self.tops = Node(val=item, next=self.tops)
      
      def pop(self):
            if self.tops:
                  self.tops = self.tops.next
                  self.mins = self.mins.next

      def min(self):
            if self.mins:
              return self.mins.val

s = MinStack()
print(s.min())
s.push(4)
print(s.min())

s.push(3)
print(s.min())
s.push(12)
print(s.min())

s.pop()
print(s.min())

