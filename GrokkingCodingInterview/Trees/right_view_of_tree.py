'''
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''

from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def right_view_of_tree(root):
	queue = deque()
	queue.append(root)
	rightViewNodes = []
	while queue:
		l = len(queue)
		for _ in range(l):
			currentNode = queue.popleft()
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
		rightViewNodes.append(currentNode)
	return rightViewNodes

root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
root = right_view_of_tree(root)
for node in root:
	print(node.val)