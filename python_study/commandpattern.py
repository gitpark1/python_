from abc import*
##command
class Command(metaclass=ABCMeta):
    @abstractmethod
    def exec(self):
        pass

##concrete command
class RobotCommand(Command):
    def __init__(self,robot,command):
        self.robot=robot
        self.command=command
    
    def exec(self):
        for x in self.command:
            if(x==1):
                self.robot.stop()
            elif(x==2):
                self.robot.run()
            elif(x==3):
                self.robot.jump()
            else:
                self.robot.exit()

##Invoker
class Invoker:
    def __init__(self):
        self.command_list=[]

    def add_command(self,command):
        self.command_list.append(command)

    def run_command(self):
        for x in self.command_list:
            x.exec()
            
##receiver
class Robot:
    def __init__(self,name):
        self.name=name
    
    def stop(self):
        print("{} is stop".format(self.name))
    
    def run(self):
        print("{} is run".format(self.name))

    def jump(self):
        print("{} is jump".format(self.name))
    
    def exit(self):
        print("{} is sleep".format(self.name))

A1 = Robot('A1')
B1 = Robot('B1')
C1 = Robot('C1')


C_A1 = RobotCommand(A1,[1,2,3])
C_B1 = RobotCommand(B1,[2,3,1])
C_C1 = RobotCommand(C1,[3,4,1])

invoker=Invoker()
invoker.add_command(C_A1)
invoker.add_command(C_B1)
invoker.add_command(C_C1)
invoker.run_command()