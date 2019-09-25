'''
Given preorder and inorder traversal of a tree, construct the binary tree.
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
#To do
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder:
        return None
    
    root = TreeNode(preorder[0])
    stack = []
    stack.append(root)
    
    pre = 1
    ino = 0
    while (pre < len(preorder)):
        curr = TreeNode(preorder[pre])
        pre += 1
        prev = None
        while stack and stack[-1].val == inorder[ino]:
            prev = stack.pop()
            ino += 1
        if prev:
            prev.right = curr
        else:
            stack[-1].left = curr
            
        stack.append(curr)
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)

    