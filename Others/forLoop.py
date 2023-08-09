from numpy import *;



arr1 = array([2,2,3,4,5,6,7])

arr2 = array([3,4,5,66,77,3])


# print(unique(arr1))
#arr = arr + arr1

# print(arr1+arr2)



arr3 = arr1.copy()

arr1 [1] = 101

print(arr1)
print(arr3)

print(id(arr3))
print(id(arr1))
