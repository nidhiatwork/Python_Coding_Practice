'''
Given a m i n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class MinPathSum(object):
    def minPathSum_DP(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    
    def minPathSum_recursive(self, grid,i,j):
        if(i == len(grid)-1 and j == len(grid[0])-1):
            return grid[i][j]
        
        if(j == len(grid[0])-1):
            return grid[i][j] + self.minPathSum_recursive(grid, i+1, j)

        if(i == len(grid)-1):
            return grid[i][j] + self.minPathSum_recursive(grid, i, j+1)

        right = self.minPathSum_memo(i,j+1,grid,cost)
        down = self.minPathSum_memo(i+1,j,grid,cost)
        return grid[i][j] + min(right, down)

    def minPathSum_memo(self, i, j, grid, cost):
        if i == len(grid)-1 and j >= len(grid[0])-1:
            cost[i][j]=grid[i][j]
            return cost[i][j]
        
        if(j == len(grid[0])-1):
            return grid[i][j] + self.minPathSum_memo(i+1, j, grid, cost)

        if(i == len(grid)-1):
            return grid[i][j] + self.minPathSum_memo(i, j+1, grid, cost)

        if i < len(grid) and j< len(grid[0]) and cost[i][j] != -1:
            return cost[i][j]
        
        right = self.minPathSum_memo(i,j+1,grid,cost)
        down = self.minPathSum_memo(i+1,j,grid,cost)
        cost[i][j] = grid[i][j] + min(right, down)
        return cost[i][j]
                
s = MinPathSum()
grid = [
  [1,3,2,1],
  [1,5,3,1],
  [4,2,5,3],
  [3,1,2,2]
]
cost = [[-1 for _ in range(len(grid[0]))]for _ in range(len(grid))]
print(s.minPathSum_memo(0, 0, grid, cost))
# print(s.minPathSum_recursive(grid,0,0))
