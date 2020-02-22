'''
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next # Remember next node
        curr_node.next = prev_node  # REVERSE! None, first time round.
        prev_node = curr_node  # Used in the next iteration.
        curr_node = next_node  # Move to next node.
    return prev_node


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
h = reverseList(head)
while h:
    print(h.val)
    h=h.next

