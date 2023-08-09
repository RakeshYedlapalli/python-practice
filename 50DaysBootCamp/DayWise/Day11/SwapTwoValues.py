def swapValues(array1):
    print((array1))
    temp = array1[0]
    array1[0] = array1[len(array1)-1]
    array1[len(array1)-1] = temp
    print(array1)

swapValues([2,4,5,6,7,4,4,12,494,5959])

