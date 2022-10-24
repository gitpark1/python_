class Monostate:
    __shared_state={'a':13}     #이건 private이 아닌가?
    
    def __init__(self):
        self.__dict__=self.__shared_state
    #본래 __dict__는 객체의 변수에 대한 값을 딕셔너리 형태로 보유하는 속성
    #위의 문장으로 인해서 같은 딕셔너리를 공유하게 되었다.


b1=Monostate()
b2=Monostate()

b1.a=44
b1.b=33

print('object b1:',b1)
print('object b2:',b2)

print('b1 state',b1.__dict__)
print('b2 state',b2.__dict__)
