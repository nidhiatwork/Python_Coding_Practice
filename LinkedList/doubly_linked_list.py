class Node():
    
    def __init__(self, value, prev=None, next=None):
        self.value=value
        self.prev=prev
        self.next=next

class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendLeft(self, value):
        n = Node(value)
        n.next = self.head
        n.prev = None
        if self.head: 
            self.head.prev = n
        else:
            self.tail = n         
        self.head = n
        self.size+=1

    def appendRight(self, value):
        n = Node(value)
        runner = self.head
        if not runner:
            self.head = n
        else:
            while(runner.next):
                runner=runner.next
            runner.next = n
            n.next = None
            n.prev = runner
        self.tail = n
        self.size +=1

    def removeByValue(self, value):
        if not self.head:
            return
        runner = self.head
        prev = None
        while runner.value!=value:
            prev = runner
            runner = runner.next
        if not prev:
            self.head = runner.next
        else:
            prev.next = runner.next
            if runner.next:
                runner.next.prev = prev
            else:
                self.tail = prev
        self.size -=1

    def get_size(self):
        runner = self.head
        count = 0
        while(runner):
            count+=1
            runner = runner.next
        return count

    def traverseLTR(self):
        runner = self.head
        print("Printing elements left to right")
        while runner:
            print(runner.value)
            runner= runner.next

    def traverseRTL(self):
        print("Printing elements right to left")
        runner = self.tail
        while runner:
            print(runner.value)
            runner= runner.prev

l = DoublyLinkedList()
l.appendLeft(4)
l.appendRight(9)
l.appendRight(3)
l.appendLeft(5)
print(l.get_size())
l.traverseLTR()
l.traverseRTL()
l.removeByValue(4)
l.traverseLTR()
l.removeByValue(3)
l.traverseLTR()
l.removeByValue(5)
l.traverseLTR()
l.removeByValue(9)
l.traverseLTR()


