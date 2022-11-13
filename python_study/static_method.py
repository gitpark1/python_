class Calc:
    count=0
    def __init__(self,a):
        self.num=a
        Calc.count+=1
    """
    def test2(self,c):      생성자 외부에서도 선언가능, 관용적으로 생성자에서 모두 처리한다
        self.c=c
        print(c)
    """
    @classmethod        #classmethod의 경우 cls 사용(self와 유사한 변수) cls로 클래스 속성에 접근
    def print_count(cls):
        cls.a=5
        print('{}번 생성'.format(cls.count))
    
    @classmethod
    def clstest(cls):
        cls.a=7
        print("clsmethod test",cls.a)
        cls.print_count()
        print("clsmethod test",cls.a)

    @staticmethod       #staic이라서 self사용 X
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def mul(a,b):
        print(a*b)

##Calc.add(10,20)
print(Calc.count)
a=Calc(10)
print(Calc.count)
Calc.print_count()
Calc.clstest()