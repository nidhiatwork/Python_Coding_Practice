'''Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

'''

from collections import Counter

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def find_cycle_start(head):
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            break
    if slow!=fast:
        return None
    fast = head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow

    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
head.next.next.next.next.next.next = head.next.next
print(find_cycle_start(head).val)