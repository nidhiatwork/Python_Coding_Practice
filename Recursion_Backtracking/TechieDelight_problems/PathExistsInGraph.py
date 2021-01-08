
from collections import deque

class Graph(object):
    def __init__(self,edges,N):
        self.adjList=[[] for _ in range(N)]
        for src,dest in edges:
            self.adjList[src].append(dest)
    
def isConnected(graph, src, dst, visited, path):
    path.append(src)
    if src == dst:
        return True
    visited[src] = True
    for w in graph.adjList[src]:
        if not visited[w] and isConnected(graph,w,dst,visited,path):
            return True
    return False

edges = [
        (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
        (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
    ]

# Number of nodes in the graph (labelled from 0 to N-1)
N = 8

# create a graph from given edges
graph = Graph(edges, N)

# stores vertex is discovered or not
visited = [False] * N

# source and destination vertex
(src, dest) = (0, 7)

# List to store the complete path between source and destination
path = deque()
# perform DFS traversal from the source vertex to check the connectivity
# and store path from the source vertex to the destination vertex
if isConnected(graph, src, dest, visited, path):
    print("Path exists from vertex", src, "to vertex", dest)
    print("The complete path is:", list(path))
else:
    print("No path exists between vertices", src, "and", dest)