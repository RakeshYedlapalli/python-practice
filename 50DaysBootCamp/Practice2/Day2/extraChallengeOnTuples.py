names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]

new_fruit=""

def listTheLowerCaseWordsInDescendingOrder(names):
    lowercase_names = [name for name in names if name.islower()]

    lowercase_names_sorted = sorted(lowercase_names, reverse=True)

    return lowercase_names_sorted

    
print(listTheLowerCaseWordsInDescendingOrder(names))