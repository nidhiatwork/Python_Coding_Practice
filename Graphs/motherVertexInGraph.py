'''A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.
'''
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

def DFSUtil(g, v, visited):
	visited[v] = True
	for n in g.graph[v]:
		if visited[n]==False:
			DFSUtil(g, n, visited)

def findMother(g):
	ans = 0
	visited = [False]*g.vertices
	for v in range(g.vertices):
		if visited[v]==False:
			DFSUtil(g, v, visited)
			ans = v
	
	visited = [False]*g.vertices
	DFSUtil(g, ans, visited)
	if False in visited:
		return -1
	return ans

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print(findMother(g))