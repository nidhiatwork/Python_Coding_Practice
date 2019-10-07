'''
Given a singly linked list, determine if it is a palindrome.

'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

        
    # compare the first and second half nodes
    while prev: # while prev and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True
        
    

head = ListNode(1)
print(isPalindrome(head))