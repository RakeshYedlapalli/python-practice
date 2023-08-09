class School:

    school = "Telusko"

    def __init__(self , m1 , m2 , m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getM1(self):
        return self.m1
    
    def getM2(self):
        return self.m2

    def getM3(self):
        return self.m3

    def setM1(self,m1):
        self.m1 = m1
    
    
    def setM2(self,m2):
        self.m2 = m2
    
    def setM3(self,m3):
        self.m3 = m3

    def avg(self):
        return self.m1 + self.m2 + self.m3

s1 = School(3,4,5)
s2 = School(2,4,5)

s2.setM1(10000)
print("M1 value is =>", s2.m1)

print(s1.avg())
print(s2.avg())