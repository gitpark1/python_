import math

class Circle:
    def __init__(self,rad=1.0):
        self.__rad=rad      #private
    
    def setRad(self,r):     #setter
        self.__rad=r    

    def getRad(self):
        return self.__rad

    def calcArea(self):
        return math.pi*self.__rad*self.__rad

    def __str__(self):
        return 'rad= {}, Area= {}'.format(self.__rad,math.pi*self.__rad*self.__rad)

    def __eq__(self,other):
        return self.__rad==other.__rad
    


c=Circle(10)
b=Circle(9)
print(c.getRad())
print(c.calcArea())
print(c)
print(c==b)

