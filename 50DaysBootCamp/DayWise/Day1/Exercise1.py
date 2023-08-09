import math 

def divide_or_square(num):
    if(num%5==0):
     print("Number is divisible by 5")   
     #return (num*num)
     return math.sqrt(num)
    else:
     print("number is not divisible by 5")
     return num%5
    # print(num%5)
    # print(num/5)


value = divide_or_square(10)
print(value)



