class Heap(object):

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]* Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        if self.isFull():
            print("Heap is full")
            return
        self.currentPosition +=1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self, index):
        parentIndex = (index-1)//2

        while parentIndex>=0 and self.heap[index]> self.heap[parentIndex]:
            self.heap[index],self.heap[parentIndex] = self.heap[parentIndex],self.heap[index]
            index = parentIndex
            parentIndex = (index-1)//2

    def heapSort(self):
        for i in range(0,self.currentPosition+1):
            print(self.heap[0])
            
            self.heap[0],self.heap[self.currentPosition-i]=self.heap[self.currentPosition-i],self.heap[0]
            self.fixDown(0, self.currentPosition-i-1)

    def fixDown(self, index, upto):
        while index<=upto:
            leftChild = 2*index+1
            rightChild = 2*index+2
            if leftChild < upto:
                childToSwap = None
                
                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild
                
                if self.heap[index]<self.heap[childToSwap]:
                    self.heap[index],self.heap[childToSwap] = self.heap[childToSwap],self.heap[index]
                else:
                    break
                index = childToSwap
            else:
                break

    def isFull(self):
        return self.currentPosition==Heap.HEAP_SIZE

h = Heap()
h.insert(24)
h.insert(12)
h.insert(10)
h.insert(2)
h.insert(1)
h.insert(9)
h.insert(8)
# h.insert(10)
# h.insert(-20)
# h.insert(0)
# h.insert(2)
print(h.heap)
h.heapSort()