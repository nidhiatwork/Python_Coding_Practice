'''There are n cities. Some of them are connected, while some are not. You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
'''
class Solution:
    def findCircleNum(self, isConnected):
        visited = [False]*len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if visited[i]==False:
                self.dfs(isConnected, visited, i)
                count+=1
        return count
    
    def dfs(self, isConnected, visited, v):
        visited[v]=True
        for i in range(len(isConnected)):
            if visited[i]==False and isConnected[v][i]:
                self.dfs(isConnected, visited, i)
            