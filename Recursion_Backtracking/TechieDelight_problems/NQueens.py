
def isSafe(board, r, c):
      for i in range(r):
            if board[i][c]=='Q':
                  return False
      i,j=r,c
      while i>=0 and j>=0:
            if board[i][j]=='Q':
                  return False
            i,j=i-1,j-1
      i,j=r,c
      while i>=0 and j<N:
            if board[i][j]=='Q':
                  return False
            i,j=i-1,j+1
      return True



def printNQueens(board, r=0):
      if r==N:
            for i in range(N):
                for j in range(N):
                      print(board[i][j],end=' ')
                print()
            print()
            return
      for i in range(N):
            if isSafe(board, r, i):
                  board[r][i] = 'Q'
                  printNQueens(board, r+1)
                  board[r][i] = '-'


N = 4
board = [['-' for _ in range(N)] for i in range(N)]
printNQueens(board)