'''Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

'''

from collections import Counter

class ListNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def check_linkedlist_palindrome(head):
    #find middle
	if not head or not head.next:
		return True
	slow,fast = head,head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	
	head_reversed = reverse(slow)
	
	while head and head_reversed:
		if head.val!=head_reversed.val:
			break
		head = head.next
		head_reversed = head_reversed.next
	
	if not head or not head_reversed:
		return True
	return False
def reverse(head):
	prev = None
	while head:
		nxt = head.next
		head.next = prev
		prev = head
		head = nxt
	return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
print(check_linkedlist_palindrome(head))