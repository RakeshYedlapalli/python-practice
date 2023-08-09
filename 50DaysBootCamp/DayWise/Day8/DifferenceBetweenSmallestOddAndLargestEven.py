def DifferenceBetweenSmallestOddAndLargestEven(listOfIntegers):
    print("before sorting data is ->", listOfIntegers)
    listOfIntegers = sorted(listOfIntegers)
    print("After sorting data is ->", listOfIntegers)
    smallestOddNumber = 0
    largesttEvenNumber = 0
    for i in range(0,len(listOfIntegers)):
        if(listOfIntegers[i] % 2 != 0):
            smallestOddNumber = listOfIntegers[i]
            break
    
    for i in reversed(range(len(listOfIntegers))):
        print("Largest even number :" , listOfIntegers[i])
        if(listOfIntegers[i] % 2 == 0):
            largesttEvenNumber = listOfIntegers[i]
            break

    print("Smallest odd number is ->" , smallestOddNumber)
    print("Largest Even number is ->" , largesttEvenNumber)
    return largesttEvenNumber - smallestOddNumber


data = [3,4,32,6,4,4,0,3,10,4,39,593,593,600]
result = DifferenceBetweenSmallestOddAndLargestEven(data)
print("Difference between two is ->", result)
