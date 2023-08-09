def flattenList(list):
    sum = 0
    for parent in list:
        for child in parent:
            sum += child

    return sum
result = flattenList([[0,0,9,3,2,4,5,6,7,5,4,3,2,2],[0,0,9,3,2,4,5,6,7,5,4,3,2,2],[0,0,9,3,2,4,5,6,7,5,4,3,2,2]])

print("sum is ->", result)


