'''On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.'''
import collections

class Solution(object): 
    def removeStones(self, stones):
        def dfs(x, y):
            seen.add((x, y))
            for new_y in groupX[x]:
                if (x, new_y) not in seen:
                    #seen.add((i, j))
                    dfs(x, new_y)
            for new_x in groupY[y]:
                if (new_x, y) not in seen:
                    #seen.add((i, j))
                    dfs(new_x, y)
                    
        seen = set ()
        island = 0
        groupX = collections.defaultdict(list)
        groupY = collections.defaultdict(list)
        
        #group the coordinates in the adjency list
        
        for x, y in stones:
            groupX[x].append(y)
            groupY[y].append(x)
        
        #print(groupX)
        #print(groupY)
            
        for (x, y) in stones:
            if (x, y) not in seen:
                #seen.add((i, j))
                dfs(x, y)
                island += 1
          
        return len(stones) - island