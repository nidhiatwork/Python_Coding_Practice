'''
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
'''

from collections import Counter

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution1(object):
	def __init__(self):
		self.ans = 0
		
	
	def diameterOfBinaryTree(self, root):
		if not root: 
			return 0
		left_height = self.diameterOfBinaryTree(root.left)
		right_height = self.diameterOfBinaryTree(root.right)
		self.ans = max(self.ans, left_height+right_height)
		print("left tree height ",root.val, "->",left_height)
		print("right tree height",root.val, "->",right_height)
		print("max height at ",root.val, "->",self.ans)
		return max(left_height, right_height) + 1 #return height at each step but save answer in separate variable called ans to acheive both objectives

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(5.1, TreeNode(5.2)))), TreeNode(3, TreeNode(6, TreeNode(7))))
#root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
s = Solution1()
s.diameterOfBinaryTree(root)
print(s.ans)