class Myiter:
    def __init__(self,end):
        self.current =0
        self.end=end

    def __iter__(self):
        print("iter")
        return self
    
    def __next__(self):
            print("next")
            if self.current < self.end:
                value = self.current
                self.current +=1
                return value
            else:
                raise StopIteration

a=Myiter(5)
for i in Myiter(5):
    print(i)