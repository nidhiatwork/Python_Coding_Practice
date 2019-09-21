'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [5,3,2,4,6,7], k = 2
     5
    / \
   3   6
 /  \    \
2    4    7
Output: 3
'''
import collections
class TreeNode:
    def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def kthSmallest_recursion(root, k):
    def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    return inorder(root)[k - 1]

def kthSmallest_iterative(root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)), TreeNode(6, None, TreeNode(7)))
print(kthSmallest_iterative(root,6))