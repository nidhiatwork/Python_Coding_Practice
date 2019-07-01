class Node():
    
    def __init__(self, value, next=None):
        self.value=value
        self.next=next


class LinkedList():
    
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        runner = self.head
        count = 0
        while(runner):
            print(runner.value)
            count+=1
            runner = runner.next
        return count
