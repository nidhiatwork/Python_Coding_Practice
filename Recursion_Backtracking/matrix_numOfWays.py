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
def func(i=0,j=0):
	global ct
	if i==m-1 and j==n-1:
		return True
	for direction in ([1,0], [0,1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isSafe(new_i, new_j):
			if func(new_i, new_j):
				ct+=1
	return False

def isSafe(i,j):
	return i<m and j<n

m,n=3,3
func()
print(ct)