'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def do(head):
    #find length
    slow,fast = head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    
    #reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    #compare both linkedlists front and prev
    front = head
    while front and prev:
        if front.val!=prev.val:
            return False
        front=front.next
        prev=prev.next
    return True
    

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
head = ListNode(1, ListNode(2))

print(do(head))
# 1->2->3 3<-2<-1
# 1->2->3->2->1
# 1->2->3->4->5