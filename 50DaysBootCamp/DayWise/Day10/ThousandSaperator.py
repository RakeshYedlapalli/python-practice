def thousandSaparator(values):

    saparatedArray = []
    for x in values:
#       print(x)
        #print('{:,}'.format(x))
        saparatedArray.append('{:,}'.format(x))

    return saparatedArray

result = thousandSaparator([1000000, 2356989, 2354672, 9878098])
print(result)