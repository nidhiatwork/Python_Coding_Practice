'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
'''


class TreeNode(object):
    def __init__(self, val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree_1(s,t):
    if s.val==t.val and checkSubtree(s,t):
        return True
    level = [s]
    while level:
        nextLevel = []   
        for node in level:
            if node.left:
                nextLevel.append(node.left)
                if node.left.val == t.val and checkSubtree(node.left,t):
                    return True
            if node.right:
                nextLevel.append(node.right)
                if node.right.val == t.val and checkSubtree(node.right,t):
                    return True
        level = nextLevel
        
    return False

def checkSubtree(s,t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val!=t.val:
        return False
    return checkSubtree(s.left,t.left) and checkSubtree(s.right,t.right)

def isSubtree_2(s, t):
    def isMatch(s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val!=t.val:
            return False
        return isMatch(s.left,t.left) and isMatch(s.right,t.right)
    
    if s is None:
        return False
    if isMatch(s, t):
        return True
    return isSubtree_2(s.left, t) or isSubtree_2(s.right, t)

def isSubtree_3(s,t):
    tree1 = preorder(s)
    tree2 = preorder(t)
    print(tree1)
    print(tree2)
    return tree1.find(tree2)>=0

def preorder(root):
    final = []
    pre(root, final)
    return '-'+'-'.join(final)

def pre(root,final):
    if root:
        final.append(str(root.val))
        pre(root.left,final)
        pre(root.right,final)
    else:
        final.append("None")



s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
t = TreeNode(4, TreeNode(1), TreeNode(2))
# s = TreeNode(12)
# t = TreeNode(2)
print(isSubtree_3(s,t))
