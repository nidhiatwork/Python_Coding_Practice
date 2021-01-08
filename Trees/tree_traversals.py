class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left=left
        self.right=right

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value)
        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.value)
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.value)


if __name__=="__main__":
    N = Node(1, Node(3, Node(6), Node(8)), Node(7, Node(10)))
    print("inorder:\n")
    print_inorder(N)
    print("preorder:\n")
    print_preorder(N)
    print("postorder:\n")
    print_postorder(N)