'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''
import collections

def orangesRotting(grid):
    d=0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    rotten = collections.deque()
    for i,row in enumerate(grid):
        for j,item in enumerate(row):
            if item==2:
                rotten.append((i,j,d))

    while rotten:
        (a,b,d)=rotten.popleft()
        for (i,j) in directions:
            if i+a>=0 and i+a<len(grid) and j+b>=0 and j+b<len(grid[0]) and grid[i+a][j+b]==1:
                grid[i+a][j+b]=2
                rotten.append((i+a,j+b,d+1))
    if any(1 in row for row in grid):
        return -1
    return d

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
