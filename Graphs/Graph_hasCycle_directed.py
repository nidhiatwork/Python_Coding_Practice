'''Given a directed graph, check whether the graph contains a cycle or not.
'''
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


def checkCycle(g):
	visited = [False]*g.vertices
	recStack = [False]*g.vertices
	for v in range(g.vertices):
		if visited[v]==False:
			if dfsCycle(g, v, visited, recStack):
				return True
	return False

def dfsCycle(g, s, visited, recStack):
	visited[s] = True
	recStack[s] = True
	for n in g.graph[s]:
		if visited[n]==False and dfsCycle(g, n, visited, recStack):
			return True
		elif recStack[n]==True:
			return True
	recStack[s]=False
	return False

def checkCycle1(g):
	visited = [False]*g.vertices
	for v in range(g.vertices):
		if visited[v]==False:
			if dfsCycle1(g, v, visited):
				return True
	return False
def dfsCycle1(g, s, visited):
	visited[s] = True
	for n in g.graph[s]:
		if visited[n]==True:
			return True
		if dfsCycle1(g, n, visited):
			return True
	visited[s]=False
	return False

	
# g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(2,0)
# g.addEdge(2,3)
# g.addEdge(3,3)

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(3,0)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,3)

print(checkCycle(g))
print(checkCycle1(g))