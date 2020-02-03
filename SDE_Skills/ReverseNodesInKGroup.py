
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
pointer = reverseKGroup(head, 3)
while(pointer):
    print(pointer.val)
    pointer = pointer.next