#Method resolution Order Left to Right


class A:

    def __init__(self):
        print("I am constructor A")

    def feature(self):
        print("I am feature from A")


class B:
    def __init__(self):
        print("I am constructor B")
    
    def feature(self):
        
        print("I am feature from B")

class C(B,A):

    def __init__(self):
        #super().__init__()
        print("I am B class constructor")

    def cFeature(self):
        super().feature()

c = C()

c.feature()
c.cFeature()