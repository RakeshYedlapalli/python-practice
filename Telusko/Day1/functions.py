def hello(x):
    print(id(x))
    x = 12
    print(id(x))


a = 10
#print(id(a))
hello(a)
print((a))


def updateListObject(list):

    list[1] = 25

list = [10,12,40]
print("Before update",list)
updateListObject(list)    
print("After update",list)