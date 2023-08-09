def returnTwoIfBothAreFloatElseReturnOne(args1 , args2):
    if(type(args1) is float and type(args2) is float):
        return 2
    else:
        return 1



result = returnTwoIfBothAreFloatElseReturnOne(3.4,4.4)
print(result)