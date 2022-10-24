class Singleton:
    def __new__(cls):
        if not hasattr(cls,'instance'):  #instance라는 속성이 없다면
            print('make instance')
            cls.instance=super().__new__(cls)   #super -> object?
        return cls.instance

#Singleton클래스의 객체는 생성될 때, if문 hasattr을 검사하게 되고, instance 속성이 존재, 객체가 존재한다면,
#그 객체를 리턴한다(1개를 넘어서 추가적인 객체가 생성되지 않는다.)

s1=Singleton()
print("object created",s1)

s2=Singleton()
print("object created",s2)