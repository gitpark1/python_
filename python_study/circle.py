import math

class Circle:
    count=0
    def __init__(self,rad):
        self.__rad=rad      #private
        Circle.count+=1
        print("init 실행",Circle.count,"\n")
    
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
    
    @classmethod
    def create(cls):
        p=Circle(5)
        print("create\n")
        return p
    
    @classmethod
    def p_count(cls):
        print("p_count_method",cls.count,"\n")
    
    @staticmethod
    def c3():
        print("static_test\n")

class two(Circle):
    def __init__(self,x):
        super().__init__(x)

    def test1(self):
        print(self.test)
"""       
print(Circle.count)
c=Circle(10)
b=Circle(9)
print(Circle.count)
print(c.getRad())
print(c.calcArea())
print(c)
print(c==b)
"""
a=Circle(5)
b=Circle(4)
print(Circle.count)
Circle.create().p_count()
a.p_count()
a.c3()