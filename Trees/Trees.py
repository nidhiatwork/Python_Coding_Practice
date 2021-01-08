class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class TreeNode:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data<node.data: 
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        
        return node.data
    
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        
        return node.data
    
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data,self.root)

    def removeNode(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.leftChild = self.removeNode(data,node.leftChild)
        elif data>node.data:
            node.rightChild = self.removeNode(data,node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                del node
                print("Returning None")
                return None
            if not node.leftChild:
                tempNode = node.rightChild
                del node
                print("Returning ",tempNode.data)
                return tempNode
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                print("Returning ",tempNode.data)
                return tempNode

            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        
        return node
    
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        
        return node

    def traverse(self):
        print("Print list")
        if self.root:
            print("In order")
            self.traverseInOrder(self.root)
            # print("Pre order")
            # self.traversePreOrder(self.root)
            # print("Post order")
            # self.traversePostOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
    
    def traversePreOrder(self, node):
        print(node.data)
        
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def traversePostOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
        
        print(node.data)

    def findByVal(self, data):
        if self.root:
            return self.findVal(data,self.root)

    def findVal(self, data, node):
        if not node:
            return None
        if data<node.data:
            return self.findVal(data,node.leftChild)
        elif data>node.data:
            return self.findVal(data,node.rightChild)
        return node.data

bst = TreeNode()
bst.insert(12)
bst.insert(5)
bst.insert(14)
bst.insert(3)
bst.insert(10)
bst.insert(7)
bst.insert(16)
bst.insert(15)
bst.insert(6)
bst.insert(2)
bst.insert(8)
bst.insert(9)
bst.insert(17)
bst.insert(14.9)
bst.insert(15.2)
bst.traverse()
bst.remove(16)
bst.traverse()
print(bst.findByVal(7))
