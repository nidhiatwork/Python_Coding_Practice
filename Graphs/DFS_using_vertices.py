class Node(object):
	def __init__(self,name):
		self.name = name
		self.adjacencyList = []
		self.visited = False
		self.predecessor = None

class DepthFirstSearch(object):

	def dfs1(self, node):
		stack = []
		node.visited = True
		stack.append(node)
		while stack:
			actual = stack.pop()
			print(actual.name)
			for neighbor in actual.adjacencyList:
				if not neighbor.visited:
					neighbor.visited = True
					stack.append(neighbor)
	
	def dfs2(self, node):
		node.visited = True
		print(node.name)
		for neighbor in node.adjacencyList:
			if not neighbor.visited:
				neighbor.visited = True
				self.dfs2(neighbor)
	
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node2.adjacencyList.append(node5)
node3.adjacencyList.append(node6)
node4.adjacencyList.append(node7)
dfs = DepthFirstSearch()
print("Using dfs1")
dfs.dfs1(node1)
print("Using dfs2")
dfs.dfs2(node1)