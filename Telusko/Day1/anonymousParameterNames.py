def person(name , age = 10):
    print(name)
    print(age)


person('rakesh',30)



#when we don't know the positions of the paramers we can pass as below

person(age =10, name = 'rakesh')

#Default values , let's say if you don't pass any value then let's take the default value as sometihng
#which we can mention as part of function parameter

person('hello ')
