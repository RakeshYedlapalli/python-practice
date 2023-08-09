from abc import ABC , abstractclassmethod

class Computer(ABC):

    @abstractclassmethod
    def process():
        pass

    @abstractclassmethod
    def process1():
        pass

class Laptop(Computer):
    def process(self):
        print("Hello I am process method")
    
    def process1(self):
        print("Hello I am process method")

#c = Computer()
l = Laptop()

l.process()