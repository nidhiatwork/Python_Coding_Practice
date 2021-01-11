'''Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.[C
'''

from collections import Counter

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head):
    if not head or not head.next:
        return head
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(middle_of_linked_list(head).val)