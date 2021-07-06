'''Given a path in the form of a rectangular matrix having few landmines arbitrarily placed (marked as 0), calculate length of the shortest safe route possible from any cell in the first column to any cell in the last column of the matrix. We have to avoid landmines and their four adjacent cells (left, right, above and below) as they are also unsafe. We are allowed to move to only adjacent cells which are not landmines. i.e. the route cannot contain any diagonal moves.'''
def shortestPath(mat):
	min_steps = [float('inf')]
	for r in range(len(mat)):
		grid = mat[:]
		steps = -1
		explorePathToEndFrom(grid, r, -1, steps, min_steps)
	return min_steps[0]

def explorePathToEndFrom(grid, r, c, steps, min_steps):
	if c==len(grid[0])-1:
		min_steps[0] = min(min_steps[0], steps)
		return
	for direction in ([1,0], [0,1], [-1,0], [0,-1]):
		new_r = r+direction[0]
		new_c = c+direction[1]
		if isValid(grid, new_r, new_c) and notAdjacentToMine(grid, new_r, new_c):
			grid[new_r][new_c] = 2
			explorePathToEndFrom(grid, new_r, new_c, steps+1, min_steps)
			grid[new_r][new_c] = 1

def isValid(grid, r, c):
	return r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==1

def notAdjacentToMine(grid, r, c):
	if r>0 and grid[r-1][c]==0:
		return False
	if r<len(grid)-1 and grid[r+1][c]==0:
		return False
	if c>0 and grid[r][c-1]==0:
		return False
	if c<len(grid[0])-1 and grid[r][c+1]==0:
		return False
	return True

arr = [
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]
    ]
print(shortestPath(arr))