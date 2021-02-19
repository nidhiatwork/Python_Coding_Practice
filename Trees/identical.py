# A class to store a binary tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to check if two given binary trees are identical or not
def isIdentical(x, y):
 
    # if both trees are empty, return true
    if x is None and y is None:
        return True
 
    # if both trees are non-empty and the value of their root node matches,
    # recur for their left and right subtree
    return (x and y) and (x.key == y.key) and \
        isIdentical(x.left, y.left) and isIdentical(x.right, y.right)
 
 
if __name__ == '__main__':
 
    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)
 
    # construct the second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)
 
    if isIdentical(x, y):
        print("The given binary trees are identical")
    else:
        print("The given binary trees are not identical")
 

