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
        return self.minDistance < other.minDistance

    def __repr__(self):
        return str(self.name)+'->'+str(self.minDistance)

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

node_u = Node("U")
node_d = Node("D")
node_a = Node("A")
node_c = Node("C")
node_i = Node("I")


edge_ad = Edge(1,node_a,node_d)
edge_da = Edge(1,node_d,node_a)
edge_dc = Edge(2,node_d,node_c)
edge_cd = Edge(2,node_c,node_d)
edge_au = Edge(3,node_a,node_u)
edge_ua = Edge(3,node_u,node_a)
edge_uc = Edge(4,node_u,node_c)
edge_cu = Edge(4,node_c,node_u)
edge_du = Edge(5,node_d,node_u)
edge_ud = Edge(5,node_u,node_d)
edge_ac = Edge(6,node_a,node_c)
edge_ca = Edge(6,node_c,node_a)
edge_ai = Edge(7,node_a,node_i)
edge_ia = Edge(7,node_i,node_a)
edge_ci = Edge(8,node_c,node_i)
edge_ic = Edge(8,node_i,node_c)


node_u.adjacencyList.append(edge_ud)
node_u.adjacencyList.append(edge_ua)
node_u.adjacencyList.append(edge_uc)

node_d.adjacencyList.append(edge_du)
node_d.adjacencyList.append(edge_dc)
node_d.adjacencyList.append(edge_da)


node_a.adjacencyList.append(edge_ad)
node_a.adjacencyList.append(edge_au)
node_a.adjacencyList.append(edge_ac)
node_a.adjacencyList.append(edge_ai)

node_c.adjacencyList.append(edge_ca)
node_c.adjacencyList.append(edge_cd)
node_c.adjacencyList.append(edge_ci)
node_c.adjacencyList.append(edge_cu)

node_i.adjacencyList.append(edge_ic)
node_i.adjacencyList.append(edge_ia)

vertexList = (node_u,node_d,node_a, node_c, node_i)

algorithm = Algorithm()
algorithm.calculateShortestPath(node_d)
algorithm.getShortestPathTo(node_i)