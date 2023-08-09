class School:
    

         def __init__(self , m1 , m2 , m3) -> None:
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3
            self.lap = self.Laptop('12GB','1TB','nice','red')

         class Laptop:   

            def __init__(self,ram,rom,config,color) -> None:
                self.ram = ram
                self.rom = rom
                self.config = config
                self.color= color
                
        

        

s1 = School(3,4,5)
s2 = School(2,4,5)

#s2.setM1(10000)
#¯print("M1 value is =>", s2.m1)

print(s1.lap.ram,s1.lap.rom,s1.lap.config,s1.lap.color)
#print(s2.avg())