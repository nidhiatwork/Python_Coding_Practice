'''Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space are marked as 1 and 0 respectively in the grid.
Examples:  
Input: [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
Output : 2
'''
ct = 0
def func(matrix, i, j):
	global ct
	if i==len(matrix)-1 and j==len(matrix[0])-1:
		return True
	for direction in ([1,0], [0,1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isSafe(matrix, new_i, new_j):
			if func(matrix, new_i, new_j):
				ct+=1
	return False

def isSafe(matrix, i,j):
	return i<len(matrix) and j<len(matrix[0]) and matrix[i][j]!=1

#Driver code
matrix =[[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]

func(matrix, 0, 0)
print(ct)