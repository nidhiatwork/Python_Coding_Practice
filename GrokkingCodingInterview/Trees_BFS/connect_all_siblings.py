'''
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.
'''

from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None, next=None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next

def connect_level_order_siblings(root):
	queue = deque()
	queue.append(root)
	prev = None
	while queue:
		currentNode = queue.popleft()
		if prev:
			prev.next = currentNode
		prev = currentNode
		if currentNode.left:
			queue.append(currentNode.left)
		if currentNode.right:
			queue.append(currentNode.right)

root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
connect_level_order_siblings(root)