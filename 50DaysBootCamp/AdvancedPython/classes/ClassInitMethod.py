class Person:
    def __init__(self, name ,age ) :
        print("I am in intilizer")
        self.name = name
        self.age = age

p1 = Person('rakesh',28)

print(p1.name)
print(p1.age)
    
