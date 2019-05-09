"""
Detect whether or not a linked list contains a cycle.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(l1):
    nodes = set()
    head = l1
    while head:
        if head in nodes:
            return True
        nodes.add(head)
        head = head.next
    return False

l1 = Node(1,Node(5, Node(7)))
# l1.next = l1
result = operate(l1)

print(result)
# while head:
#     print(head.val)
#     head = head.next

