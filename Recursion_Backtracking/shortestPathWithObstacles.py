'''In an N by N square grid, each cell is either empty (0) or blocked (1).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
Input:
[
[0,0,0],
[1,1,0],
[1,1,0]
]
output: 4
'''
def shortestPath(mat, i,j,m,n):
	shortestP = [float('inf')]
	steps = 0
	mat[i][j]=2
	explorePathToEndFrom(mat, i, j, m, n, steps, shortestP)
	return shortestP[0]

def explorePathToEndFrom(mat, i, j, m, n, steps, shortestP):
	if i==m and j==n:
		shortestP[0] = min(shortestP[0], steps)
		return
	for direction in ([1,0], [0,1], [-1,0], [0,-1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isValid(mat, new_i, new_j):
			mat[new_i][new_j] = 2
			explorePathToEndFrom(mat, new_i, new_j, m, n, steps+1, shortestP)
			mat[new_i][new_j] = 1

def isValid(grid, r, c):
	return r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==0


arr = [
[0,0,0],
[1,1,0],
[1,1,0]
]
print(shortestPath(arr,0,0,len(arr)-1,len(arr[0])-1))