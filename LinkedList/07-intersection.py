"""
Return an intersecting node if two linked lists intersect.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def findIntersection_extraSpace(l1,l2):
    nodes = set()
    while l1:
        nodes.add(l1)
        l1 = l1.next
    
    while l2:
        if l2 in nodes:
            return l2
        l2 = l2.next

def findIntersection_constantSpace(l1,l2):
    orig_l1,orig_l2 = l1,l2
    count=0
    while True:
        count+=1
        if l1==l2:
            print(count)
            return l1
        l1,l2 = l1.next,l2.next
        if not l1:
            l1 = orig_l1
        if not l2:
            l2 = orig_l2

def findIntersection_usingLengthDifference(l1, l2):
    curA,curB = l1,l2
    lenA,lenB = 0,0
    while curA is not None:
	    lenA += 1
	    curA = curA.next
    while curB is not None:
	    lenB += 1
	    curB = curB.next
    curA,curB = l1,l2
    if lenA > lenB:
	    for _ in range(lenA-lenB):
	        curA = curA.next
    elif lenB > lenA:
	    for _ in range(lenB-lenA):
	        curB = curB.next
    while curB != curA:
	    curB = curB.next
	    curA = curA.next
    return curA

l1 = Node(1,Node(5))
n = Node(3, Node(1))
l1.next.next = n
l2 = Node(2,Node(5,Node(8)))
l2.next.next.next = n
head = findIntersection_constantSpace(l1,l2)

while head:
    print(head.val)
    head = head.next

