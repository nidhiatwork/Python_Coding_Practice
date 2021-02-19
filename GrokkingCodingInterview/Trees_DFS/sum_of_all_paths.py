'''
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
'''

from collections import Counter

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_all_sum(root, path_sum):
    if not root:
        return
    path_sum = 10*path_sum + root.val
    if not root.left and not root.right:
        return path_sum
    return find_all_sum(root.left, path_sum) + find_all_sum(root.right, path_sum)
        
	

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
path = 0
print(find_all_sum(root, path))
