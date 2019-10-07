'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = headB if not p1 else p1.next
        p2 = headA if not p2 else p2.next
    return p1

headA = ListNode(4,ListNode(9, ListNode(8, ListNode(6, ListNode(2)))))
headB = ListNode(5,ListNode(0, ListNode(1)))
headB.next.next.next = headA.next.next
node = getIntersectionNode(headA, headB)
print(node.val)
