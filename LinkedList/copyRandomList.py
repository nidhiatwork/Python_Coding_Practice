'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
'''
import collections
# Definition for a Node.
class Node(object):
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList_usingDict(head):
    dic = dict()
    m = n = head
    while m:
        dic[m] = Node(m.val,None,None)
        m = m.next
    while n:
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get(head)

def copyRandomList_usingDefaultDict(head):
    dic = collections.defaultdict(lambda: Node(0))
    dic[None] = None
    n = head
    while n:
        dic[n].val = n.val
        dic[n].next = dic[n.next]
        dic[n].random = dic[n.random]
        n = n.next
    return dic[head]
A = Node(1)
B = Node(7)
C = Node(5)
D = Node(3)
A.next=B
A.random = C
B.next = C
C.next = D
B.random = A
C.random = D
D.random = B
head = copyRandomList_usingDefaultDict(A)
while head:
    print("Head: ",head.val)
    if head.next:
        print("head.next",head.next.val)
    print("head.random",head.random.val)
    head = head.next