class TrieNode(object):
	def __init__(self):
		self.is_word = False
		self.children = {}

class Trie(object):
	def __init__(self):
		self.root = TrieNode()
	
	def add(self, word):
		current_node = self.root
		for c in word:
			if c not in current_node.children:
				current_node.children[c] = TrieNode()
			current_node = current_node.children[c]
		current_node.is_word = True
			
	def exists(self, word):
		current_node = self.root
		for c in word:
			if c not in current_node.children:
				return False
			current_node = current_node.children[c]
		return current_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))