import sys
import heapq

class Edge(object):
    
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.adjacencyList = []
        self.minDistance = sys.maxsize

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

class Algorithm(object):

    def calculateShortestPath(self, startVertex):
        q = []
        startVertex.minDistance = 0
        heapq.heappush(q, startVertex)
        while q:
            actualVertex = heapq.heappop(q)
            for edge in actualVertex.adjacencyList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(q,v)
    
    def getShortestPathTo(self, targetVertex):
        print("Shortest path to vertex is ", targetVertex.minDistance)
        node = targetVertex
        while node is not None:
            print(node.name)
            node = node.predecessor

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5,node1,node2)
edge2 = Edge(8,node1,node8)
edge3 = Edge(9,node1,node5)
edge4 = Edge(15,node2,node4)
edge5 = Edge(12,node2,node3)
edge6 = Edge(4,node2,node8)
edge7 = Edge(7,node8,node3)
edge8 = Edge(6,node8,node6)
edge9 = Edge(5,node5,node8)
edge10 = Edge(4,node5,node6)
edge11 = Edge(20,node5,node7)
edge12 = Edge(1,node6,node3)
edge13 = Edge(13,node6,node7)
edge14 = Edge(3,node3,node4)
edge15 = Edge(11,node3,node7)
edge16 = Edge(9,node4,node7)

node1.adjacencyList.append(edge1)
node1.adjacencyList.append(edge2)
node1.adjacencyList.append(edge3)
node2.adjacencyList.append(edge4)
node2.adjacencyList.append(edge5)
node2.adjacencyList.append(edge6)
node8.adjacencyList.append(edge7)
node8.adjacencyList.append(edge8)
node5.adjacencyList.append(edge9)
node5.adjacencyList.append(edge10)
node5.adjacencyList.append(edge11)
node6.adjacencyList.append(edge12)
node6.adjacencyList.append(edge13)
node3.adjacencyList.append(edge14)
node3.adjacencyList.append(edge15)
node4.adjacencyList.append(edge16)

vertexList = (node1,node2,node3, node4, node5, node6, node7, node8)

algorithm = Algorithm()
algorithm.calculateShortestPath(node1)
algorithm.getShortestPathTo(node7)