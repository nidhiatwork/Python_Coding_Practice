''' Find max number in each level of binary tree
'''
from collections import deque

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMaxInEachLevelIn_BinaryTree(root):
    queue = deque()
    queue.append(root)
    res = [root.val]
    while queue is not None:
        l = len(queue)
        level = []
        for i in range(l):
            node = queue.popleft()
            if node.left:
                level.append(node.left.val)
                queue.append(node.left)
            if node.right:
                level.append(node.right.val)
                queue.append(node.right)
        res.append(max(level))
    return res
