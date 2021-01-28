'''
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.'''

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

def reverse_every_k_sublist(head,k):
	if not head or k<=1:
		return head
	
	prev,cur = None,head
	while True:
		last_node_of_prev_part = prev
		last_node_of_sub_list = cur
		i=0
		while i<k and cur:
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

		if not cur:
			break
		prev = last_node_of_sub_list
	return head
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
head = reverse_every_k_sublist(head,3)
head.printList()