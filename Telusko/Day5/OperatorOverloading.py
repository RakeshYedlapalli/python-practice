print("Hello"+" World")




def hellIWillAddTwoNumbers(self, __x: int) -> int: ...

print(hellIWillAddTwoNumbers(3,4))



class Student:

    def __init__(self, m1 , m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(a:float,b:float):

        print("Addition Called")

    

    def __sub__(student1,student2):

        print("Substraction Called")

    
    
    def __mul__(student1,student2):

        print("Multiplication Called")

s1 = Student(4,3)
s2 = Student(3,3)

print(s1+s2)
print(s1-s2)
print(s1*s2)

print(1.2+2.2)
print(1-2)