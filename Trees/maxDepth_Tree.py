'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
First approach is by recursion. Second by BFS
'''

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution_recursion:
    def maxDepth(self, root):
        if not root:
            return 0
        depth_left = self.maxDepth(root.left)
        print("Found depth_left: ",depth_left)
        depth_right = self.maxDepth(root.right)
        print("Found depth_right: ",depth_right)
        return 1 + max(depth_left, depth_right)

class Solution_BFS:
    def maxDepth(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth


root = TreeNode(3,TreeNode(9, TreeNode(5)), TreeNode(20, TreeNode(15), TreeNode(7, TreeNode(1))))

S = Solution_recursion()
print(S.maxDepth(root))
S = Solution_BFS()
print(S.maxDepth(root))