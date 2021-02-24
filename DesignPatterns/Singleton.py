class Singleton:
    _instance = None
    
    def __new__(self):
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
            self.y = 10
        return self._instance
    

# Hence all below lines return same object only
s = Singleton()
print(s)
print(s.y)

s = Singleton()
print(s)

s = Singleton()
print(s)