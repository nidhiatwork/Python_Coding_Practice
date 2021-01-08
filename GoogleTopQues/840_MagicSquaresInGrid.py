'''
grid 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).


Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
'''

def numMagicSquaresInside(grid):
    ct=0
    for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
            if isSubGridMagic(grid,i,j):
                ct+=1
    return ct

def isSubGridMagic(grid,i,j): 
    nums = set(grid[a][b] for b in range(j,j+3) for a in range(i,i+3) if grid[a][b]>=1 and grid[a][b]<=9)
    a = grid[i][j:j+3]
    b = grid[i+1][j:j+3]
    c = grid[i+2][j:j+3]
    d = [grid[x][j] for x in range(i,i+3)]
    e = [grid[x][j+1] for x in range(i,i+3)]
    f = [grid[x][j+2] for x in range(i,i+3)]
    g = [grid[x+i][y+j] for x in range(3) for y in range(3) if x==y]
    h = [grid[x+i][y+j] for x in range(2,-1,-1) for y in range(3) if x+y==2]
    if sum(a)==sum(b)==sum(c) == sum(d)==sum(e)==sum(f)==sum(g)==sum(h) and len(nums)==9:
        return True
    else:
        return False

# grid = [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# grid = [[5,5,5],[5,5,5],[5,5,5]]

# grid = [
#     [10,3,5],
#     [1,6,11],
#     [7,9,2]
#     ]
grid = [
    [3,2,9,2,7],
    [6,1,8,4,2],
    [7,5,3,2,7],
    [2,9,4,9,6],
    [4,3,8,2,5]
    ]
print(numMagicSquaresInside(grid))