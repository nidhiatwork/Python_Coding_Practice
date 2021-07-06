'''Given an undirected graph, check whether the graph contains a cycle or not.
'''
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)


def main(g):
	visited = [False]*g.vertices
	for v in range(g.vertices):
		if visited[v]==False:
			if dfs(g, v, visited, -1):
				return True
	return False

def dfs(g, s, visited, parent):
	visited[s] = True
	for n in g.graph[s]:
		if visited[n]==False:
			if dfs(g, n, visited, s):
				return True
		elif n!=parent:
			return True
	return False

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

print(main(g))
g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
print(main(g1))

