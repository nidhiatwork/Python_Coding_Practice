'''Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
matrix = [
[ 1,  5,  9],
[10, 11, 13],
[12, 13, 15]],
k = 8,
return 13.
'''
import heapq

def kthSmallest_1(matrix, k):
        l = []
        for row in matrix:
            l += row
        return sorted(l)[k-1]

def kthSmallest_2(matrix, k):
       h = [n for row in matrix for n in row]
       print((h))
       heapq.heapify(h)
       for _ in range(1,k):
              heapq.heappop(h)
       return heapq.heappop(h)

def kthSmallest_3(matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret                 

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print(kthSmallest_1(matrix,8))