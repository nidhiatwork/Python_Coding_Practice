'''
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
'''

from collections import Counter

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_path_sum(root, S):
	if not root:
		return False
	if S==root.val and root.left is None and root.right is None:
		return True
	return find_path_sum(root.left, S-root.val) or find_path_sum(root.right, S-root.val)

root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
print(find_path_sum(root, 18))