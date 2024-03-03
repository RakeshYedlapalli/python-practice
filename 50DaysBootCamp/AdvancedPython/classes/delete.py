class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
     print("Hello my name is " + self.name)


classValue = Student("rakes",20)
print(classValue.name)
print(classValue.age)

del classValue.age

print(classValue.age)



