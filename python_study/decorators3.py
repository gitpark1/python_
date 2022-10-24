def plus(x):
    def dec(func):
        def wrapper(a,b):
            r=func(a,b)
            print('{},{}'.format(x,func.__name__))
            return r
        return wrapper
    return dec

@plus(3)
def add(a,b):
    return a+b

print(add(20,30))