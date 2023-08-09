def replaceFirstAndLastIndexWithZeros(listOfData):
    print("Before replacing with zeros:", listOfData)

    listOfData[0] = 0
    listOfData[len(listOfData)-1] = 0

    print("After replacing the values ->", listOfData)


data = [3,4,5,6,7,8,8,3,3,5,6]
replaceFirstAndLastIndexWithZeros(data)

