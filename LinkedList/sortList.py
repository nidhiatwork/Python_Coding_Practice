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

def merge(h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
def sortList(head):
    if not head or not head.next:
        print("returning: ", head.val)
        return head
        

    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre, slow, fast = slow, slow.next, fast.next.next
    pre.next = None
    print("Setting {} to None".format(pre.val))
    a = sortList(head)
    b = sortList(slow)
    return merge(a, b)

head = ListNode(4,ListNode(2,ListNode(1,ListNode(3,ListNode(9)))))
head = sortList(head)
while head:
    print(head.val)
    head = head.next