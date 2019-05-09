"""
Return an intersecting node if two linked lists intersect.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(l1,l2):
    nodes = set()
    head = l1
    while head:
        nodes.add(head)
        head = head.next
    
    while l2:
        if l2 in nodes:
            return l2
        l2 = l2.next


l1 = Node(1,Node(5))
n = Node(3, Node(1))
l1.next = n
l2 = Node(2,Node(5,Node(8)))
l2.next = n
head = operate(l1,l2)

# print(result)
while head:
    print(head.val)
    head = head.next

