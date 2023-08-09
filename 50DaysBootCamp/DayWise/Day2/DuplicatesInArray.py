fruits = ['apples', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

count = 0

duplicateValues = []

for fruit1 in fruits:
    for fruit2 in fruits:
        if (fruit1 == fruit2):
            count = count+1

    if (count > 1):
        duplicateValues.append(fruit1)

        break
    count = 0    


if (len(duplicateValues) > 0):
    print(duplicateValues)
else:
    print("No duplicates found")


# if(len(fruits) != len(set(fruits))):
#     print("There are duplicates in List")
# else:
#     print("No Duplicates found in given array list")
