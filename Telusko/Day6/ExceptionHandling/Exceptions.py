a = 5
b = 0

try:
    print(a/b)
except Exception as e:
    print("You can't do zero division -> ",e)
finally:
    print("I am executed")