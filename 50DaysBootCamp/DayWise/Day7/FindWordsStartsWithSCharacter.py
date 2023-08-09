def findWordsStartsWithCharacterS(listOfWords):
    dictionary = {}
    for word in listOfWords:
        # print(word)
        if (word.lower().startswith('s')):
            if word in dictionary.keys() :
                dictionary[word] = int(dictionary[word])+1
            else:
                dictionary[word] = 1
    return dictionary

values = ["Joseph", "Nathan", "Sasha", "Kelly",
          "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
result = findWordsStartsWithCharacterS(values)
print(result)
