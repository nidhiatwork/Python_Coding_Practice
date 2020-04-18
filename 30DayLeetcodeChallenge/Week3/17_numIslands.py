'''
Given a 2d grid map of '1'grid (land) and '0'grid (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

11110
11010
11000
00000

Output: 1

11000
11000
00100
00011

Output: 3
'''
def numIslands(grid):
    if not grid:
        return 0
    r, c = len(grid), len(grid[0])
    visited = [[False for _ in range(c)] for _ in range(r)]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == 1:
                dfs(grid, i, j, visited)
                count += 1
    return count

def dfs(grid, i, j, visited):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1 or visited[i][j]:
        return
    visited[i][j]=True
    dfs(grid, i+1, j, visited)
    dfs(grid, i-1, j, visited)
    dfs(grid, i, j+1, visited)
    dfs(grid, i, j-1, visited)

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]
print(numIslands(grid))