'''Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell. A cell in given maze has value -1 if it is a blockage or dead end, else 0.
From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.
Examples: 
Input: maze[R][C] =  [[0,  0, 0, 0],
                      [0, -1, 0, 0],
                      [-1, 0, 0, 0],
                      [0,  0, 0, 0]];
Output: 4
'''

def func(matrix, i, j, curPath, ansPath):
	if i==len(matrix)-1 and j==len(matrix[0])-1:
		return True
	for direction in ([1,0], [0,1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isSafe(matrix, new_i, new_j):
			curPath.append(matrix[new_i][new_j])
			if func(matrix, new_i, new_j, curPath, ansPath):
				ansPath.append(curPath[:])
			curPath.pop()		
	return False

def isSafe(matrix, i,j):
	return i<len(matrix) and j<len(matrix[0])

matrix = [[1, 2, 3],
		 [4, 5, 6]]
		 
curPath = [matrix[0][0]]
ansPath = []
func(matrix, 0, 0, curPath, ansPath)
print(ansPath)
