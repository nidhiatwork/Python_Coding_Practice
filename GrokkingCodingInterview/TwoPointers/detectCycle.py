'''Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''

from collections import Counter
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
 
def findInt(head):
    slow = fast = head
    #find intersection
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return slow
    return None
def detectCycle(head):
    
    if not head:
        return None
    fast = findInt(head)
    if not fast:
        return None
    #find start of cycle
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow

head = ListNode(1)
print(detectCycle(head))