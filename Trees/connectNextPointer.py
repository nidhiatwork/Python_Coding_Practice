'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
'''

class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return None
    level = [root]
    while level:
        nodes = [node for node in level]            
        for i in range(len(nodes)-1):
            next = nodes[i+1]
            print("Connecting next from {} to {}".format(nodes[i].val,next.val))
            nodes[i].next = next
        nodes[-1].next=None
        nextLevel = []
        for node in level:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        level = nextLevel
    return root

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
head = connect(root)
stack=[head]

    