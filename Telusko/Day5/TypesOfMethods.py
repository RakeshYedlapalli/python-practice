class School:

    school = "Telusko"

    def __init__(self , m1 , m2 , m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return self.m1 + self.m2 + self.m3

s1 = School(3,4,5)
s2 = School(2,4,5)

print(s1.avg())
print(s2.avg())