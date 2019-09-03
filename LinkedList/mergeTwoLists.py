'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
import collections
class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

def mergeTwoLists1(l1,l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

#Complex Recursion -- try to understand
def mergeTwoLists2(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists2(l1, l2.next)
        return l2
        

l1=ListNode(1, ListNode(2, ListNode(4)))
l2=ListNode(1, ListNode(4, ListNode(5)))
cur = mergeTwoLists1(l1,l2)

while cur:
    print(cur.val,end='->')
    cur = cur.next