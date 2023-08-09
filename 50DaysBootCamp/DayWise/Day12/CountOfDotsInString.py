def countOfDotsInString(plainString):
    listOfChars = list()
    listOfChars += plainString
    count = 0
    for x in listOfChars:
        if(x == '.'):
            count +=1
    
    return count
        

result = countOfDotsInString('.r.a.k.esh.')
print(result)