'''Given a directed graph, check whether the graph contains a cycle or not using color coding.
'''
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

def main(g):
	visited = [0]*g.vertices
	for v in range(g.vertices):
		if visited[v]==0:
			if dfs(g, v, visited):
				return True
	return False

def dfs(g, s, visited):
	visited[s] = 1
	for n in g.graph[s]:
		if visited[n]==1:
			return True
		elif visited[n]==0:
			if dfs(g, n, visited):
				return True
	visited[s]=2
	return False

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

print(main(g))
g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
print(main(g1))

