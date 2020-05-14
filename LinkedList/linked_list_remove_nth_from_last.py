
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth(head, n):
    if not head:
        return head
    curr = head
    lead, follow = curr,curr
    while n>0 and lead:
        lead = lead.next
        n-=1
    if not lead:
        if n==0:
            return curr.next
        else:
            return head
    while lead and lead.next:
        lead=lead.next
        follow=follow.next
    print("at ListNode: ", follow.val)
    follow.next = follow.next.next
    return curr

l = ListNode(1, ListNode(2, ListNode(3)))
h = remove_nth(l, 2)
while h:
    print(h.val)
    h = h.next