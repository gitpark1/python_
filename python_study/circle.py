import math

class Circle:
    count=0
    def __init__(self,rad=1.0):
        self.__rad=rad      #private
        Circle.count+=1
    
    def setRad(self,r):     #setter
        self.__rad=r    

    def getRad(self):
        return self.__rad

    def calcArea(self):
        return math.pi*self.__rad*self.__rad

    def __str__(self):
        return 'rad= {}, Area= {}'.format(self.__rad,self.calcArea())

    def __eq__(self,other):
        return self.__rad==other.__rad
    

print(Circle.count)
c=Circle(10)
b=Circle(9)
print(Circle.count)
print(c.getRad())
print(c.calcArea())
print(c)
print(c==b)
print(c.object_type)
