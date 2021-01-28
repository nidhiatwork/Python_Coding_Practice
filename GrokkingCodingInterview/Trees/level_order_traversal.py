'''
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''

from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def level_order_traversal(root):
	result = []
	if not root:
		return result
	
	queue = deque()
	queue.append(root)
	while queue:
		levelSize = len(queue)
		currentLevel = []
		for _ in range(levelSize):
			currentNode = queue.popleft()
			currentLevel.append(currentNode.val)
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
		result.append(currentLevel)
	return result
	
root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
print(str(level_order_traversal(root)))