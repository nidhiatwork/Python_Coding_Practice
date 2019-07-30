'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
from queue import PriorityQueue

class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

def mergeKLists(lists):
    head = point = ListNode(0)
    q = PriorityQueue()
    for idx,l in enumerate(lists):
        if l:
            q.put((l.val, idx, l))
    while not q.empty():
        val, idx, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, idx, node))
    return head.next

l1=ListNode(2,ListNode(4,ListNode(5)))
l2=ListNode(1,ListNode(3,ListNode(4)))
l3=ListNode(3,ListNode(6))
merged = mergeKLists([l1,l2,l3])
while merged.next:
    print(merged.val, end='->')
    merged = merged.next
print(merged.val)



def mergeKLists_easy(lists):
    head = dummy = ListNode(0)
    vals = []
    for l in lists:
        while l:
            vals.append(l.val)
            l=l.next
    vals.sort()
    for val in vals:
        dummy.next = ListNode(val)
        dummy=dummy.next
    return head.next