import collections
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        stack = [head]
        for i in range(1,len(preorder)):
            node = TreeNode(preorder[i])
            if preorder[i]<stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < preorder[i]:
                    last = stack.pop()
                last.right = node
            stack.append(node)
        return head

                
s = Solution()
preorder = [13,6,4,3,5,8,9,14,15]
head = s.bstFromPreorder(preorder)
print(head.val)

