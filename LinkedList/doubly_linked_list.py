class Node():
    
    def __init__(self, value, prev=None, next=None):
        self.value=value
        self.prev=prev
        self.next=next

class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None


    def appendLeft(self, value):
        n = Node(value)
        n.next = self.head
        n.prev = None
        if self.head is not None: 
            self.head.prev = n         
        self.head = n

    def append(self, value):
        runner = self.head
        while(runner.next):
            runner=runner.next
        n = Node(value)
        runner.next = n
        n.next = None
        n.prev = runner


    def size(self):
        runner = self.head
        count = 0
        while(runner):
            print(runner.value)
            count+=1
            runner = runner.next
        return count

l = DoublyLinkedList()
l.appendLeft(4)
l.appendLeft(9)
l.appendLeft(3)
l.appendLeft(5)
print(l.size())

