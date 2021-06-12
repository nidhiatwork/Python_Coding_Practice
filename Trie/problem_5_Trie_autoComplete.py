class TrieNode:
	def __init__(self):
		self.children = {}
		self.is_word = False
	
	def insert(self, char):
		self.children[char] = TrieNode()
	
	def suffixes(self, suffix = '', sufs = []):
		if not self.children:
			sufs.append(suffix)
			return sufs
		if self.is_word and suffix:
			sufs.append(suffix)
		for child in self.children:
			sufs = self.children[child].suffixes(suffix+child, sufs)
		return sufs

	def __repr__(self):
		node = []
		for k,v in self.children.items():
			node.append(str(k)+'->'+str(v))
		return ','.join(node)

## The Trie itself containing the root node and insert/find functions
class Trie:
	def __init__(self):
		self.root = TrieNode()

	def __repr__(self):
		return str(self.root)

	def insert(self, word):
		runner = self.root
		for c in word:
			if c not in runner.children:
				runner.insert(c)
			runner = runner.children[c]
		runner.is_word = True
	
	def find(self, prefix):
		i=0
		runner = self.root
		node = None
		while runner.children:
			matched = False
			for child in runner.children:
				if i==len(prefix):
					return node
				if child==prefix[i]:
					matched = True
					i+=1
					runner = runner.children[child]
					node = runner
			if not matched:
				break
		return None


MyTrie = Trie()
wordList = [
	"ant", "anthology", "antagonist", "antonym", 
	"fun", "function", "factory", 
	"trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
	MyTrie.insert(word)

#TC 1: Positive test case
prefix = 'tri'
prefixNode = MyTrie.find(prefix)
if prefixNode:
	print('\n'.join(prefixNode.suffixes()))
else:
	print(prefix + " not found")
# e
# gger
# onometry
# pod


#TC 2: Blank prefix
prefix = ''
prefixNode = MyTrie.find(prefix)
if prefixNode:
	print('\n'.join(prefixNode.suffixes()))
else:
	print(prefix + " not found")
#  not found


#TC 3: Prefix not present 
prefix = 'act'
prefixNode = MyTrie.find(prefix)
if prefixNode:
	print('\n'.join(prefixNode.suffixes()))
else:
	print(prefix + " not found")
# act not found
