'''

'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeTwoLists_iteratively(l1,l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1=l1.next
        else:
            cur.next = l2
            l2=l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

def mergeTwoLists_recursively(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val< l2.val:
        print(l1.val," is less than ",l2.val)
        l1.next = mergeTwoLists_recursively(l1.next,l2)
        print("Move ",l1.val," to smaller between ",l1.next.val,l2.val)
        return l1
    else:
        print(l2.val," is less than ",l1.val)
        l2.next = mergeTwoLists_recursively(l1,l2.next)
        print("Move ",l2.val," to smaller between ",l1.val,l2.next.val)
        return l2

l1 = ListNode(3,ListNode(5,ListNode(6)))
l2 = ListNode(1,ListNode(2, ListNode(4, ListNode(7))))
h = mergeTwoLists_iteratively(l1,l2)
while h:
    print(h.val)
    h = h.next