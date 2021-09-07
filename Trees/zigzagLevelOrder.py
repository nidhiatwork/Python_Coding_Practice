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
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
        level = [root]
        leftToRight = False
        while level:
            nextLevel = []
            if leftToRight:
                for node in level: #[1]
                    print(node.val)
                    
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
            else:
                for node in level:
                    
                    print(node.val)
                    if node.right:
                        nextLevel.append(node.right)
                    if node.left:
                        nextLevel.append(node.left)
                    
            leftToRight = not leftToRight
            level = nextLevel
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(7)
root.right.left = Node(6)
root.left.left = Node(4)
root.left.right = Node(5)
zigzagLevelOrder(root)