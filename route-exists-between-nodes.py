"""
Find if route exists from the first node to the second node in a directed graph.
# Using BFS
"""

from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 

	def addEdge(self,u,v): 
		self.graph[u].append(v) 
	
	def isReachable(self, s, d): 
		visited =[False]*(self.V)
		queue=[]
		queue.append(s)
		visited[s] = True

		while queue: 
			n = queue.pop(0) 
			if n == d: 
				return True
			for i in self.graph[n]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True
		return False

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

u =1; v = 3

if g.isReachable(u, v): 
	print("There is a path from %d to %d" % (u,v)) 
else : 
	print("There is no path from %d to %d" % (u,v)) 

u = 3; v = 1
if g.isReachable(u, v) : 
	print("There is a path from %d to %d" % (u,v)) 
else : 
	print("There is no path from %d to %d" % (u,v)) 

