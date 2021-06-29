'''A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down. 
'''

def isSafe( maze, x, y ):
	return x >= 0 and x < len(maze) and y >= 0 and y < len(maze) and maze[x][y] ==1 and visited[x][y]==0
	
def solveMaze( maze ):
	if solveMazeUtil(maze, 0, 0) == False:
		print("Solution doesn't exist")
	else:
		for row in visited:
			print(row)
	
def solveMazeUtil(maze, x, y):
	
	if x == len(maze) - 1 and y == len(maze) - 1 and maze[x][y]== 1:
		visited[x][y] = 1
		return True
	
	for k in range(len(move_x)):
		new_x = x+move_x[k]
		new_y = y+move_y[k]
		if isSafe(maze, new_x, new_y):
			visited[new_x][new_y] = 1
			if solveMazeUtil(maze, new_x, new_y):
				return True
			visited[new_x][new_y] = 0
	return False

move_x = [1,0,-1,0]
move_y = [0,1,0,-1]
maze = [[1, 0, 1, 1],
		[1, 1, 0, 1],
		[0, 1, 0, 0],
		[1, 1, 1, 1] ]
visited = [ [ 0 for j in range(len(maze)) ] for i in range(len(maze)) ]
visited[0][0]=1
		
solveMaze(maze)
