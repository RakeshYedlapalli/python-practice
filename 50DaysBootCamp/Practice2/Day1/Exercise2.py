#write a code to convert from list of string integers to list of integers and then sum up all of them

def arrayOfStrignElements(arrayOfData):
    value = 0
    for element in arrayOfData:
        print(element)
        value +=int(element)
    
    return value+2


userInpt = input("Enter the input by comma sapearated")
print("Splitted data",userInpt.split())
result = arrayOfStrignElements(userInpt.split())
print("The final sum of given values are ->", result)