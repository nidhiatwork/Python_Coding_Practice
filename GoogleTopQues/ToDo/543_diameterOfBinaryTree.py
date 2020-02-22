'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
'''

class TreeNode(object):
        def __init__(self, val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(root):
            if not root: 
                return 0
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans, L+R)
            return 1+max(L, R)

        depth(root)
        return self.ans

root = TreeNode(1,TreeNode(2, TreeNode(4, TreeNode(5, TreeNode(7, TreeNode(9)),TreeNode(8, TreeNode(6), TreeNode(12)))), TreeNode(3, TreeNode(2), TreeNode(9, None, TreeNode(6)))),TreeNode(5))
s = Solution()
print(s.diameterOfBinaryTree(root))
