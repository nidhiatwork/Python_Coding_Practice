'''A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.
'''
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

def DFSUtil(g, s, d, visited):
	if s==d:
		return True
	visited[s] = True
	for n in g.graph[s]:
		if visited[n]==False:
			if DFSUtil(g, n, d, visited):
				return True
	return False


	

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
visited = [False]*g.vertices
print(DFSUtil(g, 5, 3, visited))