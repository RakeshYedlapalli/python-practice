def findFloatValues(a,b):

    if isinstance(a, float):
        if isinstance(b, float):
            return 2
        else:
            return 1
    elif (isinstance(b, float)):
        return 1 
    else:
        return 0      



print(findFloatValues(12.3,12.4))
print(findFloatValues(12,12))
print(findFloatValues(12,12.4))
print(findFloatValues(12.4,12))