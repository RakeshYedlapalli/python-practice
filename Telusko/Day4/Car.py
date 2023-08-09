class Car:
    wheels = 4

    def __init__(self) -> None:
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

print(c1.mil, c1.com , c1.wheels)
print(c2.mil, c2.com , c2.wheels)