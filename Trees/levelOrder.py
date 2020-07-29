'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]'''

class TreeNode:
        def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

def levelOrder_1(root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
                ans.append([node.val for node in level])
                temp = []
                for node in level:
                        temp.extend([node.left, node.right])
                level = []
                for node in temp:
                        if node:
                                level.append(node)
        return ans

def levelOrder_2(root):
        if not root:
                return []
        traversal = []
        level = [root]
        while level:
                currentNodes = []
                nextLevel = []
                for node in level:
                        currentNodes.append(node.val)
                        if node.left:
                                nextLevel.append(node.left)
                        if node.right:
                                nextLevel.append(node.right)
                traversal.append(currentNodes)
                level = nextLevel
        return traversal


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(levelOrder_1(root))