'''

'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def hasCycle_usingSet(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

def hasCycle_usingTwoPointers(head):
    slow = head
    fast = head
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast) :
            return True
    return False
        
    

head = ListNode(3,ListNode(2, ListNode(0, ListNode(4))))
last = head.next.next.next
last.next = head.next
print(hasCycle_usingTwoPointers(head))