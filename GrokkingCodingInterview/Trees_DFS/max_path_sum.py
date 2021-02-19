'''
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
'''

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution1(object):
	def __init__(self):
		self.max_sum = 0
		
	
	def find_max_path_sum(self, root):
		if not root: 
			return 0
		left_sum = self.find_max_path_sum(root.left)
		right_sum = self.find_max_path_sum(root.right)
		left_sum = max(left_sum,0) #to ignore negatives
		right_sum = max(right_sum,0)
		
		self.max_sum = max(self.max_sum, left_sum+right_sum+root.val)
		print("left tree height ",root.val, "->",left_sum)
		print("right tree height",root.val, "->",right_sum)
		print("max height at ",root.val, "->",self.max_sum)
		return max(left_sum, right_sum) + root.val #return height at each step but save answer in separate variable called ans to acheive both objectives

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(5.1, TreeNode(5.2)))), TreeNode(3, TreeNode(6, TreeNode(7))))
#root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
s = Solution1()
s.find_max_path_sum(root)
print(s.max_sum)
