
def numOfWays(m, n, dp, i=0,j=0):
    if i==m or j==n:
        return 0
    if i==m-1 and j==n-1:
        return 1
    if dp[i][j]!=0:
        return dp[i][j]
    for direction in [(1,0), (0,1)]:
        new_i = i+direction[0]
        new_j = j+direction[1]
        if new_i<m and new_j<n:
            dp[new_i][new_j] += numOfWays(m,n, dp, new_i, new_j)
    

m=7
n=3
dp = [[0 for i in range(n)] for j in range(m)]
numOfWays(m,n, dp)
print(dp[0][0])
