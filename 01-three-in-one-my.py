# Use a single array to implement three stacks.
"""
three_stacks.push(101, 0)
    three_stacks.push(102, 0)
    three_stacks.push(103, 0)
    three_stacks.push(201, 1)
    self.assertEqual(three_stacks.pop(0), 103)
    self.assertEqual(three_stacks.pop(1), 201)
    self.assertEqual(three_stacks.pop(1), None)
    self.assertEqual(three_stacks.pop(2), None)
"""

class ThreeStacks():
  def __init__(self):
        self.array = [list(),list(),list()]
        self.current = [0,1,2]

  def __str__(self):
        return str(self.array)

  def push(self, stack_no, val):
        self.array[stack_no].append(val)

  def pop(self, stack_no):
        self.array[stack_no].pop()

t = ThreeStacks()
t.push(0,10)
t.push(0,20)
t.push(0,30)
t.pop(0)
t.push(1,5)
t.push(2,13)
t.pop(2)
print(t)
