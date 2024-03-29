from collections import deque

class TreeNode:
        def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

def preorder_iterative(root):
    stack = list()
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(8)), TreeNode(6)))
preorder_iterative(root)