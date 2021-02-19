'''
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''

from collections import Counter

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_path_sum(root, S, path, paths):
	if not root:
		return
	path.append(root.val)
	if S==root.val and root.left is None and root.right is None:
		paths.append(list(path))
	else:
		print("Going left from ",root.val)
		find_path_sum(root.left, S-root.val, path, paths)
		print("Going right from ",root.val)
		find_path_sum(root.right, S-root.val, path, paths)
	path.pop()

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
paths = []
path = []
find_path_sum(root, 10, path,paths)
print(paths)