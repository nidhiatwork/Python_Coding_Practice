'''
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
'''
class BinaryMatrix(object):
        def __init__(self):
            self._matrix = []
            self.count = 0
        
        def get(self,x,y):
            if self.count<1000:
                self.count += 1
                return self._matrix[x][y]
            else:
                print("Too many calls - ",self.count)
                exit()
        
        def dimensions(self):
            return [len(self._matrix),len(self._matrix[0])]

def leftMostColumnWithOne(binaryMatrix):
    row,col = binaryMatrix.dimensions()
    i=0
    j=col-1
    ans = -1
    while i<row and j>=0:
        if binaryMatrix.get(i,j)==0:
            i+=1
        else:
            ans = j
            j-=1
    return ans


def leftMostColumnWithOne_binarySearch(binaryMatrix):
    row,col = binaryMatrix.dimensions()
    i=0
    j= col-1
    ans = -1
    while i<row:
        new_ans = binSearch(0, j, i)
        if new_ans!=-1:
            ans = new_ans
            j = new_ans
        i+=1
    return ans

def binSearch(low, high, row):
    while low<high:
        mid = low+(high-low)//2
        if binaryMatrix.get(row,mid):
            high = mid
        else:
            low=mid+1
    if binaryMatrix.get(row,low):
        return low
    return -1


binaryMatrix = BinaryMatrix()
binaryMatrix._matrix = [[0,0],[1,1]]
print(leftMostColumnWithOne(binaryMatrix))
# print(leftMostColumnWithOne_binarySearch(binaryMatrix))