'''Given an acyclic directed graph, print its vertices in topologically sorted order.
'''
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

def main(g):
	order = []
	visited = [0]*g.vertices
	for v in range(g.vertices):
		if visited[v]==0:
			dfs(g, v, visited, order)
	return order[::-1]

def dfs(g, s, visited, order):
	visited[s] = 1
	for n in g.graph[s]:
		if visited[n]==0:
			dfs(g, n, visited, order)
	order.append(s)

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(main(g))