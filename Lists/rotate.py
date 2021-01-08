'''You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]'''

def rotate_1(matrix):  # first reverse up to down, then swap the symmetry 
        matrix=matrix[::-1]
        for r in range(len(matrix)):
                for c in range(r+1,len(matrix)):
                        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return matrix

def rotate_2(matrix): 
        matrix[:] = zip(*matrix[::-1])
        return matrix
        
def rotate_3(A):
        A = A[::-1]
        print(A)
        A[:] = [[row[i] for row in A] for i in range(len(A))]
        return A

matrix = [
   [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(rotate_3(matrix))