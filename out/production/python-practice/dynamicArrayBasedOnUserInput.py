
from array import array


print("Hello user welcome to dynamic array building")
sizeOfTheArray = int(input("Hey user Enter the size of the array :"))

userArray = array('i', [])

print("Array size is =>", len(userArray))


for i in range(sizeOfTheArray):
    x = int(input("Enter the next value :"))
    userArray.append(x)


print(userArray)

userRequest = input("Do you want to search for any word?")

if(userRequest == "Yes"):
    numberToSearch = int(input("Enter the Number to search"))
    for i in userArray:
       print("Searching for word.........")
       if(i == numberToSearch):
        print("Word found")
        break;
    else:
        print("Entered word couldn't be found")


