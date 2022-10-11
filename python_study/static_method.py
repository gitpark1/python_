class Calc:
    count=0
    def __init__(self,a):
        self.num=a
        Calc.count+=1
    
    @classmethod        #classmethod의 경우 cls 사용(self와 유사한 변수) cls로 클래스 속성에 접근
    def print_count(cls):
        print('{}번 생성. num = {}'.format(cls.count,cls.num))

    @staticmethod       #staic이라서 self사용 X
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20)
print(Calc.count)
a=Calc(10)
print(Calc.count)
Calc.print_count()