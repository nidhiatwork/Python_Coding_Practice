"""
Determine whether or not a linked list is a palindrome.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(head):
    forward_head = head
    prev_head = None
    while head:
        n = Node(head.val)
        n.next = prev_head
        prev_head = n
        head = head.next
    
    while forward_head:
        if forward_head.val!=prev_head.val:
            return False
        forward_head, prev_head = forward_head.next, prev_head.next
    return True

a = Node(1,Node(2,Node(2, Node(1))))

result = operate(a)
print(result)
# while head:
#     print(head.val)
#     head = head.next

