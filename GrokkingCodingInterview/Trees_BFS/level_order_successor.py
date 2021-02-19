'''
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
'''

from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def level_order_successor(root,key):
	queue = deque()
	queue.append(root)
	while queue:
		currentNode = queue.popleft()
		if currentNode.left:
			queue.append(currentNode.left)
		if currentNode.right:
			queue.append(currentNode.right)
		if key==currentNode.val:
			break
	return queue[0].val if queue else None

root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
print(level_order_successor(root,10))