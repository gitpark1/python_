class player:
    def __init__(self,round,hit):
        self.__round=round
        self.__hit=hit
    
    def set(self,round,hit):
        self.__round=round
        self.__hit=hit

    def createMemento(self):
        return Memento(self.__round,self.__hit)

    def restore(self,memento):
        self.__round=memento.round
        self.__hit=memento.hit
    
    def print(self):
        print("round = {}, hit = {}".format(self.__round,self.__hit))

class Memento:
    def __init__(self,round,hit):
        self.round=round
        self.hit=hit

p_history=[]
p1=player(1,4)
p_history.append(p1.createMemento())
p1.set(2,10)
p_history.append(p1.createMemento())
p1.set(3,4)
p_history.append(p1.createMemento())
p1.print()
p1.restore(p_history[0])
p1.print()

