'''Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4'''

def maximalSquare(matrix) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
        return len(matrix) and max(map(max, matrix)) ** 2

def maximalSquare_1(matrix):
    r=len(matrix)
    if not r:
        return 0
    c=len(matrix[0])
    n=min(r,c)
    ones=[[0 for _ in range(c+1)]for _ in range(r+1)]
    for i in range(1,r+1):
        for j in range(1,c+1):
            ones[i][j] = matrix[i-1][j-1]-0 + ones[i-1][j]+ones[i][j-1]-ones[i-1][j-1]
    for s in range(n,0,-1):
        for i in range(r-s+1):
            for j in range(c-s+1):
                if(ones[i+s][j+s]-ones[i+s][j]-ones[i][j+s]+ones[i][j] == s*s) :
                    return s*s
    return 0



matrix = [
[1,0,1,0,0],
[1,0,1,1,1],
[1,1,1,1,1],
[1,0,0,1,0]
]
print(maximalSquare_1(matrix))