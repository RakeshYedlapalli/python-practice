
# def isEvenNumber(value):

#     if(value%2==0):
#         return True
#     else:
#         return False



listOfData = [2,4,5,6,7,7,292,9,4]
evens = list(filter(lambda a : a%2==0,listOfData))
print(evens)


#add the +2 to all the even numbers

double = list(map(lambda n: n+2, evens))
print(double)