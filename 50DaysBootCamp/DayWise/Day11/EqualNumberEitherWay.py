def isNumberEqualEitherWay(string1, string2):
    #number = input("enter the number")
    #firstString = string1[::-1]
    secondString = string2[::-1]
    if(string1 == secondString):
        return True
    else:
        return False
    
result = isNumberEqualEitherWay('loves','evol')
print(result)