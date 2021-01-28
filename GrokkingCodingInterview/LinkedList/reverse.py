'''Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
'''

from collections import Counter

class ListNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def printList(self):
		while self:
			print(self.val, end='->')
			self = self.next
		print('None')

def reverse(head):
	if not head or not head.next:
		return head
	prev = None
	cur = head
	while cur:
		next = cur.next
		cur.next = prev
		prev = cur
		cur = next
	return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
head = reverse(head)
head.printList()