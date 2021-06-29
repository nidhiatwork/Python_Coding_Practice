'''Given a square maze containing positive numbers, find all paths from a corner cell (any of the extreme four corners) to the middle cell. We can move exactly n steps from a cell in 4 directions i.e. North, East, West and South where n is value of the cell,
[ 3, 5, 4, 4, 7, 3, 4, 6, 3 ]
[ 6, 7, 5, 6, 6, 2, 6, 6, 2 ]
[ 3, 3, 4, 3, 2, 5, 4, 7, 2 ]
[ 6, 5, 5, 1, 2, 3, 6, 5, 6 ]
[ 3, 3, 4, 3, 0, 1, 4, 3, 4 ]
[ 3, 5, 4, 3, 2, 2, 3, 3, 5 ]
[ 3, 5, 4, 3, 2, 6, 4, 4, 3 ]
[ 3, 5, 1, 3, 7, 5, 3, 6, 4 ]
[ 6, 2, 4, 3, 4, 5, 4, 5, 1 ]
Output:
(0, 0) -> (0, 3) -> (0, 7) -> 
(6, 7) -> (6, 3) -> (3, 3) -> 
(3, 4) -> (5, 4) -> (5, 2) -> 
(1, 2) -> (1, 7) -> (7, 7) ->
(7, 1) -> (2, 1) -> (2, 4) -> 
(4, 4) -> MID
'''
directions = ['N', 'E', 'W', 'S']
def findPathsToMid(arr):
	corners = [[0,0], [0,len(arr)-1], [len(arr)-1,0], [len(arr)-1, len(arr)-1]]
	visited = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
	for i,j in corners:
		curPath = [(i,j)]
		ans = []
		visited[i][j]=1
		pathFoundToMidFromCorner(i,j, curPath, ans, arr, visited)
		visited[i][j]=0
		for path in ans:
			print(path)
def pathFoundToMidFromCorner(i,j,curPath, ans, arr, visited):
	global directions
	if i==len(arr)//2 and j==len(arr)//2:
		return True
	for direction in directions:
		new_i = i
		new_j = j
		if direction=='N':
			new_i-=arr[i][j]
		elif direction=='E':
			new_j+=arr[i][j]
		elif direction =='W':
			new_j-=arr[i][j]
		else:	
			new_i+=arr[i][j]
		if isSafe(arr,new_i,new_j, visited):
			curPath.append((new_i,new_j))
			visited[new_i][new_j] = 1
			if pathFoundToMidFromCorner(new_i,new_j,curPath, ans, arr, visited):
				ans.append(curPath[:])
			visited[new_i][new_j] = 0
			curPath.pop()
	return False

def isSafe(arr, i, j, visited):
	return i>=0 and i<len(arr) and j>=0 and j<len(arr) and visited[i][j]==0

# arr = [
# 	[1,1,1],
# 	[1,1,1],
# 	[1,1,1]
# ]
arr = [
[ 3, 5, 4, 4, 7, 3, 4, 6, 3 ],
[ 6, 7, 5, 6, 6, 2, 6, 6, 2 ],
[ 3, 3, 4, 3, 2, 5, 4, 7, 2 ],
[ 6, 5, 5, 1, 2, 3, 6, 5, 6 ],
[ 3, 3, 4, 3, 0, 1, 4, 3, 4 ],
[ 3, 5, 4, 3, 2, 2, 3, 3, 5 ],
[ 3, 5, 4, 3, 2, 6, 4, 4, 3 ],
[ 3, 5, 1, 3, 7, 5, 3, 6, 4 ],
[ 6, 2, 4, 3, 4, 5, 4, 5, 1 ]
]
findPathsToMid(arr)