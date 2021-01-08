class Node(object):
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)
        
        node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))

        return self.settleViolations_afterInsert(data, node)

    def settleViolations_afterInsert(self, data, node):
        balance = self.calcbalance(node)
        
        #Left left heavy situation --> right totation
        if balance>1 and data<node.leftChild.data:
            print("Left left heavy situation...")
            return self.rotateRight(node)
        
        #Right right heavy situation --> left totation
        if balance < -1 and data>node.rightChild.data:
            print("Right right heavy situation...")
            return self.rotateLeft(node)
        
        #Left right heavy situation
        if balance>1 and data > node.leftChild.data:
            print("Left right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        
        #Right left heavy situation
        if balance<-1 and data<node.rightChild.data:
            print("Right left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        
        return node 

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node
        if data<node.data:
            node.leftChild = self.removeNode(data,node.leftChild)
        elif data>node.data:
            node.rightChild = self.removeNode(data,node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing leaf node: ",node.data)
                del node
                return None

            if not node.leftChild:
                print("Removing node: ",node.data)
                tempNode = node.rightChild
                del node
                return tempNode
            
            if not node.rightChild:
                print("Removing node: ",node.data)
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with left and right children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return None   # if tree had just one node, you should return None
        
        node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))

        return self.settleViolations_afterRemove(node)

    def settleViolations_afterRemove(self, node):
        balance = self.calcbalance(node)

        #left left heavy situation
        if balance>1 and self.calcbalance(node.leftChild)>=0:
            return self.rotateRight(node)
        #right right heavy situation
        if balance<-1 and self.calcbalance(node.rightChild)<=0:
            return self.rotateLeft(node)
        #left right heavy situation
        if balance>1 and self.calcbalance(node.leftChild)<0:
            node.leftChild = self.rotateLeft(node)
            return self.rotateRight(node)
        # right left heavy situation
        if balance<-1 and self.calcbalance(node.leftChild)>=0:
            self.rightChild = self.rotateRight(node)
            return self.rotateLeft(node)
        
        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

    def calculateHeight(self, node):
        if not node:
            return -1
        return node.height
    
    # if it returns > 1, means left heavy --> make right rotation
    # if it returns < -1, means right heavy --> make left rotation
    def calcbalance(self, node):
        if not node:
            return 0

        return self.calculateHeight(node.leftChild) - self.calculateHeight(node.rightChild)

    def rotateRight(self, node):
        print("Rotate on the right node: ",node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))

        tempLeftChild.height = 1 + max(self.calculateHeight(tempLeftChild.leftChild), self.calculateHeight(tempLeftChild.rightChild))
        
        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotate on the right node: ",node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))

        tempRightChild.height = 1 + max(self.calculateHeight(tempRightChild.leftChild), self.calculateHeight(tempRightChild.rightChild))
        
        return tempRightChild

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

t = AVL()
t.insert(11)
t.insert(7)
t.insert(12)
t.insert(5)
t.insert(9)
t.insert(8)
t.insert(10)
t.traverse()
print("Remove 8")
t.remove(8)
t.remove(11)
t.traverse()