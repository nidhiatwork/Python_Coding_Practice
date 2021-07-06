'''Return an edge that can be removed so that the resulting graph is a tree of n nodes without any cycles.
'''
import collections
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            visited = set()
            if self.dfs(u, v, graph, visited):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
            
    def dfs(self, source, target, graph, visited):
        visited.add(source)
        if source == target: 
            return True
        for nei in graph[source]:
            if nei not in visited:
                if self.dfs(nei, target,graph, visited):
                    return True

edges = [[1,2],[1,3],[2,3]]
s = Solution()
print(s.findRedundantConnection(edges))