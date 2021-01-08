'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
'''
import collections
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric_recursive(root):
    return isMirror(root,root)
    
def isMirror(t1,t2):
    if (t1 is None and t2 is None):
        return True
    if (t1 is None or t2 is None):
        return False
    return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)


def isSymmetric_iterative_deque(root): #Not sure if works
    q = collections.deque()
    q.append((root,root))
    while (q):
        t1,t2 = q.popleft()
        if (t1 is None and t2 is None):
            continue
        if (t1 is None or t2 is None):
            return False
        if (t1.val != t2.val):
            return False
        q.append((t1.left,t2.right))
        q.append((t1.right,t2.left))
    return True


def isSymmetric_iterative_levelOrder(root):
    if not root:
        return True
    level = [root]
    while level:
        currentNodes = []
        nextLevel = []
        for node in level:
            if node.left:
                nextLevel.append(node.left)
                currentNodes.append(node.left.val)
            else:
                currentNodes.append(None)
            if node.right:
                nextLevel.append(node.right)
                currentNodes.append(node.right.val)
            else:
                currentNodes.append(None)
        level = nextLevel
        if not any(level):
            return True
        if not verify_mirror(currentNodes):
            return False
        print(currentNodes)
    return True

def verify_mirror(a):
    i,j=0,len(a)-1
    while i<j:
        if a[i]!=a[j]:
            return False
        i,j=i+1,j-1
    return True

# root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
# root = TreeNode(1, TreeNode(2,None, TreeNode(3)), TreeNode(2, TreeNode(3), None))
root = TreeNode(1, TreeNode(2,TreeNode(4, TreeNode(5),TreeNode(6)), TreeNode(3, TreeNode(7), TreeNode(8))), TreeNode(2, TreeNode(3, TreeNode(8), TreeNode(7)),TreeNode(4, TreeNode(6), TreeNode(5))))
print(isSymmetric_iterative_levelOrder(root))
