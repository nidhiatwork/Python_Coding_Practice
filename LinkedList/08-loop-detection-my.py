"""
Detect whether or not a linked list contains a cycle.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def findCycle_usingSet(head):
    nodes = set()
    while head:
        if head in nodes:
            return True
        nodes.add(head)
        head = head.next
    return False

def findCycle_usingTwoPointers(head):
    slow_p,fast_p=head,head
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return True
    return False

head = Node(1,Node(5, Node(7)))
# head.next.next = head
result = findCycle_usingTwoPointers(head)

print(result)
# while head:
#     print(head.val)
#     head = head.next

