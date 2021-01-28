'''
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
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

def rotate_list(head,k):
	if not head or not head.next or k<=1:
		return head
	len=0
	prev,cur = None,head
	while cur:
		prev = cur
		cur = cur.next
		len+=1
	last_node = prev
	k=k%len
	i=0
	runner = head
	while i<len-k:
		prev = runner
		runner = runner.next
		i+=1
	prev.next = None
	last_node.next = head
	return runner

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
head = rotate_list(head,3)
head.printList()