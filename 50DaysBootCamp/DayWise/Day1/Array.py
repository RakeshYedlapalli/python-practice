listOfData = ['rakesh','rajesh','surehs','mahesh']
tupleData = (20,30,93,9439,2929,3939,1,2,4,4,5,6,10)
dictionaryData = {"id":"123","name":"rakesh","firstName":"rakesh","lastName":"Yedlapalli"}

listOfData =  sorted(listOfData)
tupleData = sorted(tupleData)
dictionaryData = sorted(dictionaryData)
#listOfData.sort()
print(listOfData)
print(tupleData)
print(dictionaryData)


print("types of objects")

print("type is -> ", type(listOfData))
print("type is -> ", type(tupleData))
print("type is -> ", type(dictionaryData))

print(type(int("7")))