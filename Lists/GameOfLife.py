'''
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''
def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """

    # Neighbors array to find 8 neighboring cells for a given cell
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

    rows = len(board)
    cols = len(board[0])

    # Create a copy of the original board
    copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

    # Iterate through board cell by cell.
    for row in range(rows):
        for col in range(cols):

            # For each cell count the number of live neighbors.
            live_neighbors = 0
            for neighbor in neighbors:

                r = (row + neighbor[0])
                c = (col + neighbor[1])

                # Check the validity of the neighboring cell and if it was originally a live cell.
                # The evaluation is done against the copy, since that is never updated.
                if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                    live_neighbors += 1

            # Rule 1 or Rule 3        
            if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = 0
            # Rule 4
            if copy_board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 1
    print(board)

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
gameOfLife(board)