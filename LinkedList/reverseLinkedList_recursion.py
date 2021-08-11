class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            runner = self.head
            while runner.next:
                runner=runner.next
            runner.next = node        

    def display(self):
        runner = self.head
        while runner.next:
            print(runner.val, end="->")
            runner = runner.next
        print(runner.val)

    def reverse(self, node):
        if not node:
            return None
        if not node.next:
            self.head = node
            return node
        result = self.reverse(node.next)
        result.next = node
        node.next = None
        return node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display()
ll.reverse(ll.head)
ll.display()
