'''Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell. A cell in given maze has value -1 if it is a blockage or dead end, else 0.
From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.
Examples: 
Input: maze[R][C] =  [[0,  0, 0, 0],
                      [0, -1, 0, 0],
                      [-1, 0, 0, 0],
                      [0,  0, 0, 0]];
Output: 4
'''
ct=0
def func(maze, i=0, j=0):
	global ct
	if i==len(maze)-1 and j==len(maze[0])-1:
		return True
	for direction in ([1,0], [0,1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isSafe(maze, new_i, new_j):
			if func(maze, new_i, new_j):
				ct+=1
	return False

def isSafe(maze,i,j):
	return i<len(maze) and j<len(maze[0]) and maze[i][j]!=-1

maze = [[0,  0, 0, 0],
		[0, -1, 0, 0],
		[-1, 0, 0, 0],
		[0,  0, 0, 0]]

if maze[0][0]==-1 or maze[-1][-1]==-1:
	print(0)
else:
	func(maze)
	print(ct)