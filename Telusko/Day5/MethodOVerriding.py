class A:
    def methodOverriding(self):
        print("This is from Parent class or base class or super class")


class B(A):
    pass
    # def methodOverriding():
    #     print("This is sub class or child class")


b = B()

b.methodOverriding()