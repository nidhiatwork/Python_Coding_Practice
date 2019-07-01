"""
Implement a class that acts as a single stack made out of multiple stacks
which each have a set capacity.
"""

class MultiStack:
      def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

      def push(self, item):
        if self.stacks and len(self.stacks[-1])<self.capacity:
          self.stacks[-1].append(item)
        else:
              self.stacks.append([item])
      
      def pop(self):
            if len(self.stacks):
                  self.stacks[-1].pop()
                  if len(self.stacks[-1])==0:
                        del self.stacks[-1]

      def popAt(self, stack_no):
            if stack_no<len(self.stacks):
                  self.stacks[stack_no].pop()

m = MultiStack(3)
m.push(3)
m.push(3)
m.push(3)
m.push(3)
m.push(3)
m.push(3)
m.push(3)
m.push(3)
m.push(3)
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()

