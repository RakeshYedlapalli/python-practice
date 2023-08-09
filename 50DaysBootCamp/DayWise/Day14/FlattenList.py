def flattenList(list):
    finalList = []
    for parent in list:
        for child in parent:
            finalList.append(child)

    return finalList
result = flattenList([[0,0,9,3,2,4,5,6,7,5,4,3,2,2],[0,0,9,3,2,4,5,6,7,5,4,3,2,2],[0,0,9,3,2,4,5,6,7,5,4,3,2,2]])

print(result)


