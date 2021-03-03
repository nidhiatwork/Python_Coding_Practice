"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Given 1.2.3.4, you should return the list as 2.1.4.3.
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def swap_nodes_by_value(head):
    temp = head 
         
    # There are no nodes in ilnked list 
    if temp is None: 
        return 
        
    # Traverse furthur only if there are at least two 
    # left 
    while(temp is not None and temp.next is not None): 

        # Swap val of node with its next node's val 
        temp.val, temp.next.val = temp.next.val, temp.val  
            
        # Move temo by 2 fro the next pair 
        temp = temp.next.next

def swap_nodes_recursive(head):
    if not head or not head.next:
        return head 
  
    remaing = head.next.next
  
    newhead = head.next
  
    head.next.next = head 
  
    head.next = swap_nodes_recursive(remaing) 
  
    return newhead

def swap_nodes_iterative(head):
    if head is None or head.next is None:
        return head
 
    curr = head
    prev = None
 

    while curr and curr.next:
 
        temp = curr.next
        curr.next = temp.next
        temp.next = curr
 
        if prev is None:
            head = temp
        else:
            prev.next = temp
 
        prev = curr
        curr = curr.next
 
    return head

n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
h = swap_nodes_iterative(n)
while h:
    print(h.val)
    h=h.next