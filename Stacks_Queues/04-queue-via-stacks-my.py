"""

Implement a queue using two stacks.

"""

class QueueViaStacks:
      def __init__(self):
            self.in_stack = []
            self.out_stack=[]

      def push(self, item):
            self.in_stack.append(item)

      def remove(self):
        if len(self.out_stack)==0:
            while len(self.in_stack)>0:
                  self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
  
q = QueueViaStacks()
q.push(1)
q.push(2)
q.remove()

q.push(3)
q.remove()
q.remove()

q.push(1)
q.push(1)