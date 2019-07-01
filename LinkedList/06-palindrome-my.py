"""
Determine whether or not a linked list is a palindrome.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(head):
    forward = head
    prev = None
    while head:
        n = Node(head.val)
        n.next = prev
        prev = n
        head = head.next
    
    while forward:
        if forward.val!=prev.val:
            return False
        forward, prev = forward.next, prev.next
    return True

a = Node(1,Node(2,Node(2, Node(1))))

result = operate(a)
print(result)
# while head:
#     print(head.val)
#     head = head.next

