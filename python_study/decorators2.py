def trace(func):
    def wrapper(*arg,**karg):
        r=func(*arg,**karg)
        print("{}".format(func.__name__))
        return r
    return wrapper

@trace
def get_max(*arg):
    return max(*arg)

@trace
def get_min(**karg):
    return min(karg.values())

a=[1,2,3,4,5]
print(get_max(a))
print(get_min(b=10,c=2))