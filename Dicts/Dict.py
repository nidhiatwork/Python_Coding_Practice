class Dict(object):

    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size
    
    def put(self, key, value):
        index = self.hashfunction(key)
        while self.keys[index]:
            if self.keys[index]==key:
                self.values[index] = value
            index = (index+1)%self.size
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hashfunction(key)
        while self.keys[index]:
            if self.keys[index]==key:
                return self.values[index]
            index = (index+1)%self.size
        return None

    def hashfunction(self, key):
        sum = 0
        key=str(key)
        for pos in range(len(key)):
            sum+=ord(key[pos])
        return sum%self.size

d = Dict()
d.put(2,5)
d.put(3,15)
d.put(4,8)
d.put(1,6)
print(d.get(4))