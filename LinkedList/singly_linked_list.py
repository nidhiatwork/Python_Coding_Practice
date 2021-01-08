class Node():
    
    def __init__(self, value, next=None):
        self.value=value
        self.next=next


class LinkedList():
    
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def insertAtStart(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insertAtEnd(self, value):
        new_node = Node(value)
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        self.size +=1
    
    def remove(self, value):
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
        self.size -=1

    def traverse(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next

l = LinkedList()
l.insertAtStart(3)
l.insertAtEnd(7)
l.insertAtEnd(12)
l.remove(3)
l.insertAtStart(5)
l.insertAtStart(3)
l.traverse()

