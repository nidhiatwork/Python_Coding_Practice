'''Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
'''

from collections import Counter

class ListNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def hasCycle(head):
	slow,fast = head,head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow==fast:
			return True
	return False
<<<<<<< HEAD
	
=======

>>>>>>> 88bf0bda88764f957d7d0656826c2ad9033373ba

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
head.next.next.next.next.next.next = head.next.next
print(hasCycle(head))