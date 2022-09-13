from abc import ABC , abstractclassmethod

class shape:
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimeter(self):
        pass

class square(shape):
    def __init__(self,s):
        self.side=s
    def area(self):
        print(self.side**2)
    def perimeter(self):
        print(self.side*4)
s=square(4)
s.area()
s.perimeter()