# Program to reverse a doubly linked list 

# A node of the doublly linked list 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.prev = None

class DoublyLinkedList: 
	# Constructor for empty Doubly Linked List 
	def __init__(self): 
		self.head = None

	# Function reverse a Doubly Linked List 
	def reverse(self): 
		prev = None
		current = self.head 
		
		# Swap next and prev for all nodes of 
		# doubly linked list 
		while current is not None: 
			prev = current.prev 
			current.prev = current.next
			current.next = prev 
			current = current.prev 

		# Before changing head, check for the cases like 
		# empty list and list with only one node 
		if prev is not None: 
			self.head = prev.prev 
		
	# Given a reference to the head of a list and an 
	# integer,inserts a new node on the front of list 
	def push(self, new_data): 

		# 1. Allocates node 
		# 2. Put the data in it 
		new_node = Node(new_data) 

		# 3. Make next of new node as head and 
		# previous as None (already None) 
		new_node.next = self.head 

		# 4. change prev of head node to new_node 
		if self.head is not None: 
			self.head.prev = new_node 

		# 5. move the head to point to the new node 
		self.head = new_node 


	def printList(self, node): 
		while(node is not None): 
			print(node.data)
			node = node.next

# Driver program to test the above functions 
dll = DoublyLinkedList() 
dll.push(2) 
dll.push(4) 
dll.push(8) 
dll.push(10) 

print("\nOriginal Linked List")
dll.printList(dll.head) 

# Reverse doubly linked list 
dll.reverse() 

print("\n Reversed Linked List")
dll.printList(dll.head) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
