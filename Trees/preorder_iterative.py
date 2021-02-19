from collections import deque

class TreeNode:
        def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

def preorder_iterative(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val)
        if node.right:
            q.appendleft(node.right)
        if node.left:
            q.appendleft(node.left)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(8)), TreeNode(6)))
preorder_iterative(root)