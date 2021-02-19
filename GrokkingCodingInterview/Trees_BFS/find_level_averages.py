'''
Given a binary tree, populate an array to represent the averages of all of its levels.
'''

from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_level_averages(root):
	result = []
	if not root:
		return result
	queue = deque()
	queue.append(root)
	while queue:
		levelSize = len(queue)
		currentLevelSum = 0
		for _ in range(levelSize):
			currentNode = queue.popleft()
			currentLevelSum+=currentNode.val
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
		result.append(currentLevelSum/levelSize)
	return result
	
root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
print(find_level_averages(root))