'''Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

'''

from collections import Counter

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def printList(self):
        while self:
            print(self.val, end='->')
            self = self.next
        print("None")

def reorder(head):
    slow,fast = head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    
    prev = None
    while slow:
        nxt = slow.next
        slow.next=prev
        prev = slow
        slow = nxt
    
    start = head
    while prev:
        nxt = start.next
        prev_next = prev.next
        start.next = prev
        prev.next = nxt
        start = nxt
        prev = prev_next
    if start.next:
        start.next = None
    return head
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
reorder(head)
head.printList()