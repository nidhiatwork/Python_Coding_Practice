"""
#Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(head, x):
    curr,tail = head,head
    while curr:
        next = curr.next
        if curr.val < x:
            curr.next = head
            head = curr;  
        else:  
            tail.next = curr
            tail = curr
        curr = next;  
    tail.next = None 
  
    return head


n = Node(1,Node(4,Node(3,Node(2,Node(5,Node(2))))))
head = operate(n, 3)
while head:
    print(head.val)
    head = head.next
