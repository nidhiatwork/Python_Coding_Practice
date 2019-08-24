'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True'''

def isToeplitzMatrix_1(matrix):
      groups = {}
      for r, row in enumerate(matrix):
          for c, val in enumerate(row):
              if r-c not in groups:
                groups[r-c] = val
              elif groups[r-c] != val:
                return False
      return True

def isToeplitzMatrix_2(matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

def isToeplitzMatrix(A):
        for i in range(len(A)-1):
              for j in range(len(A[0])-1):
                    if A[i][j]!=A[i+1][j+1]:
                          return False
        return True
                    

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
  ]
print(isToeplitzMatrix(matrix))