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

class ChairFactory():
    @staticmethod
    def getChair(type):
        try:
            if type=="Big":
                return BigChair()
            raise AssertionError("Not valid type")
        except AssertionError as e:
            print(e)

f = ChairFactory.getChair("Big")
print(f.get_dimensions())

