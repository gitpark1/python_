class test:
    def __init__(self,a=10,b=10):
        self.a=a
        self.b=b
    def test2(self):
        print(self.__dict__)
        self.__dict__={'A':12,'B':20}

c=test()
c.test2()
c.test2()
c.a=30
c.test2()
c.test2()
