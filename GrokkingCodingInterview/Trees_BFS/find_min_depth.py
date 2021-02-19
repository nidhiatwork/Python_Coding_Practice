'''
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
'''

from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_min_depth(root):
	min_length = 0
	if not root:
		return min_length
	queue = deque()
	queue.append(root)
	while queue:
		min_length+=1
		level = len(queue)
		for _ in range(level):
			currentNode = queue.popleft()
			if not currentNode.left and not currentNode.right:
				return min_length
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
		


root = TreeNode(12, TreeNode(7), TreeNode(1, TreeNode(10), TreeNode(5)))
print(find_min_depth(root))