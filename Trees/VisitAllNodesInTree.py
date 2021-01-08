class TreeNode(object):
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

def visitAllNodes(root):
    stack = [root]
    print(root.val)
    while stack:

            node = stack.pop()
            print("removing: ",node.val)

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                print("Adding :",node.left.val)
                stack.append(node.left)
            if node.right:
                print("Adding : ",node.right.val)
                stack.append(node.right)

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
visitAllNodes(root)