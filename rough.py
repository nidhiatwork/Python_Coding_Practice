'''
Reverse a singly linked list.
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

class ListNode:
        def __init__(self, x, next=None):
            self.val = x
            self.next = next

def reverseList(head):
    pass

root = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        