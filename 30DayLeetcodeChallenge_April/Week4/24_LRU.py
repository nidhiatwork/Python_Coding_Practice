'''	
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
	
	get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
	put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. The cache is initialized with a positive capacity.
'''
import collections
class LRU(object):

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value

lru = LRU(2)
lru.put(1,1)
lru.put(2,2)
lru.put(3,3)
lru.get(1)
lru.put(4,4)
lru.put(5,5)
lru.get(4)
lru.put(6,6)
for k,v in lru.dic.items():
    print(k,v)