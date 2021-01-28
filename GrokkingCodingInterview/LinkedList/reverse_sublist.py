'''
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

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

def reverse_sublist(head, p, q):
	if p==q:
		return head
	prev,cur = None, head
	i=0
	while i<p-1:
		prev = cur
		cur = cur.next
		i+=1
	last_node_of_first_part = prev
	last_node_of_sub_list = cur

	i=0
	while i<q-p+1:
		next = cur.next
		cur.next = prev
		prev = cur
		cur = next
		i+=1
	
	if last_node_of_first_part:
		last_node_of_first_part.next = prev
	else:
		head = prev
	
	last_node_of_sub_list.next = cur
	return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = reverse_sublist(head, 3,4)
head.printList()