class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name}({self.age})"    

    def helloWorld (self):
        print("Method called", self)

p1 = Person('rakesh',29)

print(p1)
p1.helloWorld()
