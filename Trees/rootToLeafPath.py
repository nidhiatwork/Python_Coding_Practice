# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)

def printRootToLeafPaths(node, path):

    # base case
    if node is None:
        return
 
    # include the current node to the path
    path.append(node.val)
 
    # if a leaf node is found, print the path
    if not node.left and not node.right:
        print(list(path))
 
    # recur for the left and right subtree
    printRootToLeafPaths(node.left, path)
    printRootToLeafPaths(node.right, path)
 
    # remove the current node after the left, and right subtree are done
    path.pop()
 

#main function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.left.right = Node(8)
	path = []
	print(printRootToLeafPaths(root, path))

# Python code is contributed by Sumit Bhardwaj