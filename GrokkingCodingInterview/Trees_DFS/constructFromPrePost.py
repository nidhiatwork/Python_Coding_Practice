class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root
    
    def printPreOrder(self, root):
        if root:
            print(root.val)
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    
# root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
s = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
root = s.constructFromPrePost(pre,post)
s.printPreOrder(root)