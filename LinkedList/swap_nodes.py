"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def swap_nodes(head):
    if not head or not head.next:
        return head 

    node = head.next
    
    curr = head.next  
    prev = head
    while True:
            next = curr.next
            curr.next = prev  
            if not next or not next.next:
                prev.next = next; 
                break; 
            prev.next = next.next;  
            prev = next; 
            curr = prev.next
    return node

n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
h = swap_nodes(n)
while h:
    print(h.val)
    h=h.next