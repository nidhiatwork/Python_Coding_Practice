'''
matrix matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
'''

def isToeplitzMatrix_1(matrix):
    for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                print("compare: ",i,j,matrix[i][j],matrix[i+1][j+1])
                if matrix[i][j]!=matrix[i+1][j+1]:
                        return False
    return True
                
def isToeplitzMatrix_2(matrix):
    groups = {}
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r-c not in groups:
                groups[r-c] = val
            elif groups[r-c] != val:
                return False
    return True

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(isToeplitzMatrix_1(matrix))
