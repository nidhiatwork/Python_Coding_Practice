from abc import ABCMeta, abstractstaticmethod

class Chair(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimensions(self):
        """xyz"""

class BigChair(Chair):
    def __init__(self):
        self.height =10
        self.width =20
        self.length = 30
    
    def get_dimensions(self):
        return self.height, self.width, self.length

c = BigChair()
print(c.get_dimensions())
