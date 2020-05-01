class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        n = len(arr)
        def dfs(i, node):
            if not node or i == n or arr[i] != node.val:
                return False
            if i == n - 1 and not (node.left or node.right):
                return True
            return dfs(i+1, node.left) or dfs(i+1, node.right)
        return dfs(0, root)