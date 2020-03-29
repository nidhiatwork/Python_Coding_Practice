class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack ==[]
    
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.sizeStack())
print("Popped: ",s.pop())
print("Popped: ",s.pop())
print("Peek: ",s.peek())
print(s.sizeStack())