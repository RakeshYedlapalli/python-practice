def findBiggestOddNumberInGivenStringArray(stringArray):
    to_array = [char for char in stringArray]
    sorted(to_array)
    print(to_array)
    biggestOddNumber = 0

    for i in reversed(range(len(to_array))):
        if (int(to_array[i]) % 2 != 0):
            biggestOddNumber = to_array[i]
            break

    return biggestOddNumber



data = '2356'
result  =  findBiggestOddNumberInGivenStringArray(data)
print(result)
