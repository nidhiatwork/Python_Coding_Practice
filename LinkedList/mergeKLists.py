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

def mergeKLists_priorityQueue(lists):
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

def mergeSortedLists(lists):
    if not lists:
        return
    if len(lists)==1:
        return lists[0]
    mid = len(lists)//2
    l = mergeSortedLists(lists[:mid])
    r = mergeSortedLists(lists[mid:])
    return merge(l,r)
	
def merge(l,r):
	head = runner = ListNode(0)
	while l and r:
		if l.val<r.val:
			runner.next = l
			l=l.next
		else:
			runner.next = r
			r=r.next
		runner = runner.next
	runner.next = l or r
	return head.next

l1=ListNode(2,ListNode(4,ListNode(5)))
l2=ListNode(1,ListNode(3,ListNode(4)))
l3=ListNode(3,ListNode(6))
merged = mergeKLists_priorityQueue([l1,l2,l3])
while merged.next:
    print(merged.val, end='->')
    merged = merged.next
print(merged.val)

def mergeKLists_values(lists):
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