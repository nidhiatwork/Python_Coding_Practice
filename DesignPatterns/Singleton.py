class Singleton:
    __instance = None
    
    def __init__(self):
        if Singleton.__instance:
            raise Exception("This is Singleton!")
        else:
            Singleton.__instance = self
    
    @staticmethod
    def getInstance():
        if not Singleton.__instance:
            Singleton()
        return Singleton.__instance
    

# Hence all below lines return same object only
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)