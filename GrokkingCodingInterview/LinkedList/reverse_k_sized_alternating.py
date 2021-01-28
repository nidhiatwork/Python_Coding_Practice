'''
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
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

def reverse_k_sized_alternating(head,k):
	prev, cur = None, head
	while True:
		last_node_of_prev_part = prev
		last_node_of_sub_list = cur
		i=0
		while cur and i<k:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
			i+=1
		
		if last_node_of_prev_part:
			last_node_of_prev_part.next = prev
		else:
			head = prev
		
		last_node_of_sub_list.next = cur
		i=0
		while i<k and cur:
			prev = cur
			cur = cur.next
			i+=1
		if not cur:
			break
	return head
		


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
head = reverse_k_sized_alternating(head, 2)
head.printList()