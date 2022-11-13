from abc import*
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def set_next(self,handler):
        pass
    @abstractmethod
    def handle(self,request):
        pass
class AbstractHandler(Handler):
    ##_next_handler = None
    def set_next(self,handler):
        self._next_handler = handler
        return self._next_handler
    @abstractmethod
    def handle(self,request):
        if self._next_handler:
            print("next handler",self._next_handler)
           ## print(AbstractHandler._next_handler)        ##클래스변수값은 유지(None)
            print(request)
            return self._next_handler.handle(request)
        return None

class MonKeyHandler(AbstractHandler):
    def handle(self,request):
        if request =="Banana":
            return "Monkey : I'll eat the {}".format(request)
        else:
            return super().handle(request)
class SquirrelHandler(AbstractHandler):
    def handle(self,request):
        if request =="Nut":
            return print("Squirrel: I'll eat the {}".format(request))
        else:
            return super().handle(request)    

monkey=MonKeyHandler()
squirrel=SquirrelHandler()
monkey.set_next(squirrel)
monkey.handle("Nut")
