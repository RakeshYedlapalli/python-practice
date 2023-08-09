array = [3,4,6,7,8,95,33,34,566,12]


def search(array , value):

    i = 0
    while(i < len(array)):

        if value == array[i]:
            return True
        i = i+1
    return False


if search(array,3):
    print("Found the value")
else:
    print("Not found")