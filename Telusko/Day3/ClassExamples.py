class Computer:

    integerValue = 10
    def configuration(self):

        print("I am good laptop with 16GB memory and 8GB",self)


computerObject = Computer()
computerObject.integerValue = 26
#print("Integer value is =>", computerObject.integerValue)
computerObject1 = Computer()
computerObject2 = Computer()
computerObject3 = Computer()
Computer.configuration(computerObject)
Computer.configuration(computerObject1)
Computer.configuration(computerObject2)
Computer.configuration(computerObject3)


#other way to access the methods are

computerObject1.configuration()
print(type(computerObject))