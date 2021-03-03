'''
Sort a linked list in O(n log n) time using constant space complexity.

Input: 4->2->1->3
Output: 1->2->3->4

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
#To do
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head
    # divide list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    # cut down the first part
    slow.next = None
    h1 = sortList(head)
    h2 = sortList(second)
    return merge1(h1, h2)


def merge1(h1, h2):
    dummy = ListNode(0)
    runner = dummy
    while h1 and h2:
        if h1.val < h2.val:
            dummy.next = h1
            h1 = h1.next
        else:
            dummy.next = h2
            h2 = h2.next
        dummy = dummy.next
    dummy.next = h1 or h2
    return runner.next


def merge(h1, h2):
    if not h1 or not h2:
        return h1 or h2
    if h1.val > h2.val:
        h1, h2 = h2, h1
    # get the return node "head"
    head = pre = h1
    h1 = h1.next
    while h1 and h2:
        if h1.val < h2.val:
            h1 = h1.next
        else:
            nxt = pre.next
            pre.next = h2
            tmp = h2.next
            h2.next = nxt
            h2 = tmp
        pre = pre.next
    # h1 and h2 at least one is None
    pre.next = h1 or h2
    return head

head = ListNode(4,ListNode(2,ListNode(1,ListNode(3,ListNode(9)))))
head = sortList(head)
while head:
    print(head.val)
    head = head.next