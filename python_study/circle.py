from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
import math
class Circle:
    def __init__(self,rad=1.0):
        self.__rad=rad      #private
    
    def setRad(self,r):     #setter
        self.__rad=r    

    def getRad(self):
        return self.__rad

    def calcArea(self):
        return math.pi*self.__rad*SENDFILE_FALLBACK_READBUFFER_SIZE

    def calcCircum(self):
        return 2.0*math.pi*self.__rad

c1 = Circle(10)
print(c1.getRad())
print(c1.calcArea())
print(c1.calcCircum())

