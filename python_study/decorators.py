def decorator1(func):
    def wrapper():
        print('decorator')
        print("A1")
        func()
        print("A2")
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        print("B2")
        func()
        print("B2")
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

hello()
