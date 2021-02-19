from collections import deque
class TreeNode():
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right


def find_lowest_common_ancestor(root, p, q):
	parent_dict =dict()
	queue = deque()
	queue.append(root)
	parent_dict[root] = None
	while(queue):
		node = queue.popleft()
		if node.left:
			queue.append(node.left)
			parent_dict[node.left] = node
		if node.right:
			queue.append(node.right)
			parent_dict[node.right] = node
	
	ancestor = set()
	while p:
		ancestor.add(p)
		p = parent_dict[p]
	
	while q not in ancestor:
		q = parent_dict[q]
	
	return q

def find_lowest_common_ancestor_fromList(root, nodes):
	parent_dict =dict()
	queue = deque()
	queue.append(root)
	parent_dict[root] = None
	while(queue):
		node = queue.popleft()
		if node.left:
			queue.append(node.left)
			parent_dict[node.left] = node
		if node.right:
			queue.append(node.right)
			parent_dict[node.right] = node
	i=0
	p,q= nodes[i], nodes[i+1]
	while i<len(nodes)-1:
		anc = findLowestAnc_subjob(parent_dict, p,q)
		i+=1
		p = anc
		q = nodes[i+1]
	return anc


def findLowestAnc_subjob(parent_dict, p,q):
	ancestor = set()
	while p:
		ancestor.add(p)
		p = parent_dict[p]
	
	while q not in ancestor:
		q = parent_dict[q]
	
	return q