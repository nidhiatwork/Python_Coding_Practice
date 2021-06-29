'''Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9'''
def solveSudoku(grid):
	if solve_grid(grid)==True:
		for row in grid:
			print(row)
	else:
		print('No solution is possible for this grid.')

def solve_grid(grid):
	row,col = get_empty_spot(grid)
	if row==-1 and col==-1:
		return True
	for val in range(1,10):
		if isSafe(grid, row, col, val):
			grid[row][col] = val
			if solve_grid(grid):
				return True
			grid[row][col] = 0

def isSafe(grid, row, col, val):
	
	if val in grid[row]:
		return False
	
	for r in range(9):
		if grid[r][col]==val:
			return False
	
	row = (row//3)*3
	col = (col//3)*3
	for i in range(3):
		for j in range(3):
			if grid[row+i][col+j]==val:
				return False
	return True

def get_empty_spot(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j]==0:
				return i,j
	return -1,-1

grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

solveSudoku(grid)