class ListNode(object):
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

class FindMiddle(object):
    def findMiddleNode(self, head):
        sp = head
        fp = head
        while fp:
            if not fp.next:
                break
            elif fp.next and not fp.next.next:
                sp = sp.next
                break
            else:
                fp = fp.next.next
                sp = sp.next
        return sp

h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
f = FindMiddle()
c = f.findMiddleNode(h)
print(c.val)
