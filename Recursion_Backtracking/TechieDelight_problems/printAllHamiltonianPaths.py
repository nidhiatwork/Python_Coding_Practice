# class to represent a graph object:
class Graph:

	# Constructor
	def __init__(self, edges, N):

		# A List of Lists to represent an adjacency list
		self.adjList = [[] for _ in range(N)]

		# add edges to the undirected graph
		for (src, dest) in edges:
			self.adjList[src].append(dest)
			self.adjList[dest].append(src)


def printAllHamiltonianPaths(g, v, visited, path, N):

	# if all the vertices are visited, then hamiltonian path exists
	if len(path) == N:
		# print hamiltonian path
		print(path)
		return

	# Check if every edge starting from vertex v leads to a solution or not
	for w in g.adjList[v]:

		# process only unvisited vertices as hamiltonian
		# path visits each vertex exactly once
		if not visited[w]:
			visited[w] = True
			path.append(w)

			# check if adding vertex w to the path leads to solution or not
			printAllHamiltonianPaths(g, w, visited, path, N)

			# Backtrack
			visited[w] = False
			path.pop()


if __name__ == '__main__':

	# List of graph edges as per above diagram
	edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

	# Set number of vertices in the graph
	N = 4

	# create a graph from edges
	g = Graph(edges, N)

	# starting node
	start = 0

	# add starting node to the path
	path = [start]

	# mark start node as visited
	visited = [False] * N
	visited[start] = True

	printAllHamiltonianPaths(g, start, visited, path, N)
