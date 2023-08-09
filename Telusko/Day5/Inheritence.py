class A:
    def feature1():
        print("I am feature 1")
    
    def feature2():
        print("I am feature 2")

class B(A):

    def feature3():
        print("I am feature 3")

    
    def feature4():
        print("I am feature 4")



class C(B,A):
    def feature5():
        print("I am feature 5")

a = A

b = B

c = C

c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()