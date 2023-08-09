def primeNumbersOfGivenRange():
    rangeBetween = input("Enter a range: ")
    listOfPrimeNumbers = []
    count = 0
    for i in range(1, int(rangeBetween)):

        for j in range(1, i+1):
            print("i,j ", i, j)
            if (i % j == 0):
                count += 1
        print("=========", count)

        if (count == 2):
            listOfPrimeNumbers.append(i)
        count = 0

    return listOfPrimeNumbers


result = primeNumbersOfGivenRange()
print(result)
