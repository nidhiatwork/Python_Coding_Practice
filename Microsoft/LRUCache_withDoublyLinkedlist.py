class Node(object):
	def __init__(self, results):
		self.results = results
		self.prev = None
		self.next = None
	def __repr__(self):
		return str(self.results)

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	
	def __repr__(self):
		ans=[]
		runner = self.tail
		while runner is not None:
			ans.append(runner.results)
			runner=runner.next
		return '->'.join(ans)

	def move_to_front(self, node):
		if self.tail==self.head or self.head==node:
			return
		elif self.tail==node:
			self.tail=self.tail.next
			self.tail.prev = None
			self.head.next = node
			node.prev = self.head
			node.next = None
			self.head = node
		else:
			node.prev.next = node.next
			node.next.prev = node.prev
			self.head.next = node
			node.prev = self.head
			node.next = None
			self.head = node
			
	def append_to_front(self, node):
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.head.next = node
			node.prev = self.head
			self.head = node

	def remove_from_tail(self): 
		if not self.tail:
			return
		self.tail = self.tail.next
		if not self.tail:
			self.head = None

class Cache(object):
	def __init__(self, MAX_SIZE):
		self.MAX_SIZE = MAX_SIZE
		self.size = 0
		self.lookup = {}  # key: query, value: node
		self.linked_list = LinkedList()
	def get(self, query):
		node = self.lookup.get(query)
		if not node:
			return None
		self.linked_list.move_to_front(node)
		return node.results
	def set(self, results, query):
		node = self.lookup.get(query)
		if node is not None:
			node.results = results
			self.linked_list.move_to_front(node)
		else:
			if self.size == self.MAX_SIZE:
				self.lookup.pop(self.linked_list.tail.query, None)
				self.linked_list.remove_from_tail()
			else:
				self.size += 1
			new_node = Node(results)
			self.linked_list.append_to_front(new_node)
			self.lookup[query] = new_node
c = Cache(3)
c.set('1','A')
print(c.get('A'))
c.set('3','C')
c.set('2','B')
print(c.get('B'))
print(c.get('C'))
