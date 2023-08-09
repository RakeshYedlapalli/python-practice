class A:

    def __init__(self) -> None:
        print("I am constructor A")

class B(A):

    def __init__(self) -> None:
        super().__init__()
        print("I am B class constructor")
    def hello():
        print("Hello")

a = B()