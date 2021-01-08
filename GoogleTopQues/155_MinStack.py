'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
import sys

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self,data):
        self.stack.append(data)
        if not self.min_stack or data<self.min_stack[-1]:
            self.min_stack.append(data)
        else:
            self.min_stack.append(self.min_stack[-1])
    
    def top(self):
        return self.stack[-1]

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() 
minStack.pop()
minStack.top()     
minStack.getMin()