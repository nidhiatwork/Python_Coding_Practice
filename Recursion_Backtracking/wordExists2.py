'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
def exist(board, word):
	if not board:
		return False
	for i in range(len(board)):
		for j in range(len(board[0])):
			if dfs(board, i, j, word):
				return True
	return False

# check whether can find word, start at (i,j) position    
def dfs(board, i, j, word, idx=0):
	if idx==len(word):
		return True
	if word[idx]!=board[i][j]:
		return False
	tmp = board[i][j]
	board[i][j] = '#'
	for direction in ([1,0], [0,1], [-1,0], [0,-1]):
		new_i = i+direction[0]
		new_j = j+direction[1]
		if isValid(board, new_i, new_j):
			if dfs(board, new_i, new_j, word, idx+1):
				return True
	board[i][j] = tmp
	return False

def isValid(board, i, j):
	return i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j]!='#'
board = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'ABCB'
print(exist(board,word))