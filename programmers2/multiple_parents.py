class A:
    def pro(self):
        print("A")
class B(A):
    def pro(self):
        print("B")
class C(A):
    def pro(self):
        print("C")

class D(C,B):
    pass

a=D()
a.pro()
    