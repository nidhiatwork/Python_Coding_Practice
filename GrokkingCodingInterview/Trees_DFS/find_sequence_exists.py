'''
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''

from collections import Counter

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_sequence_exists(root, sequence, pos):
	if not root:
		return False
	if root.val!=sequence[pos] or pos>=len(sequence):
		return False
	if not root.left and not root.right and pos==len(sequence)-1:
		return True
	return find_sequence_exists(root.left, sequence, pos+1) or find_sequence_exists(root.right, sequence, pos+1)


    

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6, TreeNode(7))))
#root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))
sequence = [1,2,6]
print(find_sequence_exists(root, sequence, pos=0))