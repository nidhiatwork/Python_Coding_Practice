# Below lists details all 8 possible movements from a cell
# (top, right, bottom, left and 4 diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# Function to check if it is safe to go to cell (x, y) from current cell.
# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed
def isSafe(x, y, processed):
	return (0 <= x < M) and (0 <= y < N) and not processed[x][y]


# A recursive function to generate all possible words in a boggle
def searchBoggle(board, words, processed, i, j, path=""):

	# mark current node as processed
	processed[i][j] = True

	# update the path with the current character and insert it into the set
	path = path + board[i][j]
	words.add(path)

	# check for all 8 possible movements from the current cell
	for k in range(8):
		# skip if cell is invalid or it is already processed
		if isSafe(i + row[k], j + col[k], processed):
			searchBoggle(board, words, processed, i + row[k], j + col[k], path)

	# mark current node as unprocessed
	processed[i][j] = False


# Function to search for given set of words in a boggle
def searchInBoggle(board, input):

	# construct a matrix to store whether a cell is processed or not
	processed = [[False for x in range(N)] for y in range(M)]

	# construct a set to store all possible words constructed from the matrix
	words = set()

	# generate all possible words in a boggle
	for i in range(M):
		for j in range(N):
			# consider each character as a starting point and run DFS
			searchBoggle(board, words, processed, i, j)

	# for each word in the input list, check whether it is present in the set
	print([word for word in input if word in words])


if __name__ == '__main__':

	board = [
		['M', 'S', 'E'],
		['R', 'A', 'T'],
		['L', 'O', 'N']
	]

	(M, N) = (len(board), len(board[0]))

	words = ["STAR", "NOTE", "SAND", "STONE"]
	searchInBoggle(board, words)
