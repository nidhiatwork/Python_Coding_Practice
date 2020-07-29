'''
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

Given a tree T, and two nodes p,q - find the lowest common ancestor.
'''

class TreeNode(object):
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        
def lowestCommonAncestor(root,p,q):
    stack = [root]

    # Dictionary for parent pointers
    parent = {root: None}

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:

        node = stack.pop()

        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    #Print out everything in parent
    for k,v in parent.items():
        if k and v:
            print(k.val,":",v.val)
    
    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
        ancestors.add(p)
        p = parent[p]

    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(lowestCommonAncestor(root,root.left,root.left.right.right).val)