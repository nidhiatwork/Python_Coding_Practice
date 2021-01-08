'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    ans, level = [], [root]
    left_to_right = True
    while level:
            nodes = [node.val for node in level]
            if not left_to_right:
                nodes.reverse()
            ans.append(nodes)
            temp = []
            for node in level:
                    temp.extend([node.left, node.right])
            level = []
            for node in temp:
                    if node:
                            level.append(node)
            left_to_right = not left_to_right
    return ans
        
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(zigzagLevelOrder(root))