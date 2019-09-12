'''Given a binary tree, return the inorder traversal of its nodes' values.
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal_recursion(root):
    vals = []
    def doTraversal(root):
        if root:
            if root.left:
                doTraversal(root.left)
            vals.append(root.val)
            if root.right:
                doTraversal(root.right)
    doTraversal(root)
    return vals

def inorderTraversal_iteration(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

root = TreeNode(1,TreeNode(2,TreeNode(4), TreeNode(5)),TreeNode(3,TreeNode(6)))
print(inorderTraversal_recursion(root))
print(inorderTraversal_iteration(root))
