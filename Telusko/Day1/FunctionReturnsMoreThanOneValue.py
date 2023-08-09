def functionReturnsMoreThanOneValue(list):

    even = 0
    odd = 0
    for i in list:

        if (i % 2 == 0):
            even += 1
        else:
            odd += 1

    return even, odd


even, odd = functionReturnsMoreThanOneValue([2, 4, 5, 9, 10, 13, 15, 17])
#16 ,59
print("Even : {} and Odd : {}".format(even,odd))
