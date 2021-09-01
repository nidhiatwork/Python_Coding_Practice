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

class Node:
        def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
        def __str__(self):
                return self.val

def pathToLeaf(root, path):
        if not root.left and not root.right:
                print(list(path))
                return
        for node in root.left, root.right:
                if node:
                        path.append(node.val)
                        pathToLeaf(node, path)
                        path.pop()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(4)
root.left.left = Node(7)
root.left.right = Node(6)
path = [root.val]
pathToLeaf(root, path)