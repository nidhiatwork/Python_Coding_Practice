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
def dfs(board, i, j, word):
    print("Checking for word: ",word)
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        print("Incorrect values of i,j or board[i,j]")
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    up = dfs(board, i-1, j, word[1:])
    print("Up is: ",up)
    down = dfs(board, i+1, j, word[1:])
    print("Down is: ",down)
    left = dfs(board, i, j-1, word[1:])
    print("Left is: ",left)
    right= dfs(board, i, j+1, word[1:])
    print("Right is: ",right)
    board[i][j] = tmp
    print("Returning: ",up or down or left or right)
    return up or down or left or right

board = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'SEED'
print(exist(board,word))