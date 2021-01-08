# Check if it is possible to go to (x, y) from current position. The
# function returns false if the cell has value 0 or already visited
def isSafe(mat, visited, x, y):
	return not (mat[x][y] == 0 or visited[x][y])


# if not a valid position, return false
def isValid(x, y):
	return M > x >= 0 and N > y >= 0


# Find Shortest Possible Route in a Matrix mat from source cell (0, 0)
# to destination cell (x, y)

# 'min_dist' stores length of longest path from source to destination
# found so far and 'dist' maintains length of path from source cell to
# the current cell (i, j)

def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):

	# if destination is found, update min_dist
	if i == x and j == y:
		return min(dist, min_dist)

	# set (i, j) cell as visited
	visited[i][j] = 1

	# go to bottom cell
	if isValid(i + 1, j) and isSafe(mat, visited, i + 1, j):
		min_dist = findShortestPath(mat, visited, i + 1, j, x, y, min_dist, dist + 1)

	# go to right cell
	if isValid(i, j + 1) and isSafe(mat, visited, i, j + 1):
		min_dist = findShortestPath(mat, visited, i, j + 1, x, y, min_dist, dist + 1)

	# go to top cell
	if isValid(i - 1, j) and isSafe(mat, visited, i - 1, j):
		min_dist = findShortestPath(mat, visited, i - 1, j, x, y, min_dist, dist + 1)

	# go to left cell
	if isValid(i, j - 1) and isSafe(mat, visited, i, j - 1):
		min_dist = findShortestPath(mat, visited, i, j - 1, x, y, min_dist, dist + 1)

	# Backtrack - Remove (i, j) from visited matrix
	visited[i][j] = 0

	return min_dist


if __name__ == '__main__':

	mat = [
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	]

	M = N = 10

	# construct a matrix to keep track of visited cells
	visited = [[0 for x in range(N)] for y in range(M)]

	min_dist = findShortestPath(mat, visited, 0, 0, 7, 5, float('inf'), 0)

	if min_dist != float('inf'):
		print("The shortest path from source to destination has length", min_dist)
	else:
		print("Destination can't be reached from source")
