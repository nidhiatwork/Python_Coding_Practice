'''Find the longest possible route in a matrix
Given a rectangular path in the form of a binary matrix, find the length of the longest possible route from source to destination by moving to only non-zero adjacent positions, i.e., We can form the route from positions having their value as 1. Note there should not be any cycles in the output path.'''
def longestPath(mat, i,j,m,n):
	longestP = [-float('inf')]
	steps = 0
	mat[i][j]=2
	explorePathToEndFrom(mat, i, j, m, n, steps, longestP)
	return longestP[0]

def explorePathToEndFrom(mat, i, j, m, n, steps, longestP):
	if i==m and j==n:
		longestP[0] = max(longestP[0], steps)
		if longestP[0] ==23:
			print()
		return
	for direction in ([1,0], [0,1], [-1,0], [0,-1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isValid(mat, new_i, new_j):
			mat[new_i][new_j] = 2
			explorePathToEndFrom(mat, new_i, new_j, m, n, steps+1, longestP)
			mat[new_i][new_j] = 1

def isValid(grid, r, c):
	return r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==1


arr = [
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
    ]
print(longestPath(arr,0,0,1,7))