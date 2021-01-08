import collections

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    queue = collections.deque()
    queue.append([0, 0, 1])
    while queue:
        i, j, length = queue.popleft()
        if (i, j) == (n-1, n-1):
            return length
        l = ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
        for i, j in l:
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                queue.append([i, j, length+1])
                grid[i][j] = 1
    return -1

a = [
    [0,0,0],
    [1,1,0],
    [1,1,0]
    ]
print(shortestPathBinaryMatrix(a))