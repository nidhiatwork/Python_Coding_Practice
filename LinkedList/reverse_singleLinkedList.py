'''
Reverse a singly linked list.
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

class ListNode:
        def __init__(self, x, next=None):
            self.val = x
            self.next = next

def reverseLinkedList_iteration(head):
    curr = head
    prev = None
    while curr:
       nxt = curr.next
       curr.next = prev
       prev = curr
       curr = nxt
    return prev
    
def reverseLinkedList_recursion(head):
    if not head or not head.next: 
        return head
    p = reverseLinkedList_recursion(head.next)
    head.next.next = head
    head.next = None
    return p

root = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed = reverseLinkedList_recursion(root)
while reversed:
    print(reversed.val, end='->')
    reversed = reversed.next