def functionVariableLengthNotFixed(a,*n):
    print(a)

    c = a
    for i in n:
        c += i
        print(c)
    



#functionVariableLengthNotFixed(1,2,4,5,6,7,7,8,8,7,4,4,4,3)


def functionVariableLengthNotFixedKeyValues(name, **data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)


functionVariableLengthNotFixedKeyValues('naveen',age=28,city='mumbai',state='telangana',pincode='507158')