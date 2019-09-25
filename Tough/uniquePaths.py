'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

def uniquePaths(m, n):
    aux = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            aux[i][j] = aux[i][j-1]+aux[i-1][j]
    return aux[-1][-1]


print(uniquePaths(3,2))
