def indexOfLongestWord(listOfStrings):
    longestWord = max(listOfStrings , key = len)
    print("Longest word is =>" + longestWord)
    return listOfStrings.index(longestWord)
    #print(listOfStrings)


strings = ["rajesh","rakesdfadfafdasfdsh","mahfdsdfadfasfdasdfasdfadsesh"]

result = indexOfLongestWord(strings)
print(result)