'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
'''

import sys
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    def depth(self, node, ans):
        if not node: 
            return 0
        L = self.depth(node.left, ans)
        R = self.depth(node.right, ans)
        ans[0] = max(ans[0], L+R)
        print("Node: ",node.val, " L: ", L, " R: ",R," return: ",1 + max(L, R)," ans: ", ans[0])
        return 1 + max(L, R)

    def diameterOfBinaryTree(self, root):
        ans = [0]
        self.depth(root, ans)
        return ans[0]

s = Solution()
root = TreeNode(1,TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6, TreeNode(8, TreeNode(11, TreeNode(15), TreeNode(16)), TreeNode(12)), TreeNode(9, TreeNode(13))), TreeNode(7, TreeNode(14, TreeNode(17), TreeNode(18)), TreeNode(10, TreeNode(19), TreeNode(20, TreeNode(21))))))
print(s.diameterOfBinaryTree(root))