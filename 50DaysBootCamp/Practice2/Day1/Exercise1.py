def executeSomething(number):
    if(number%5==0):
        print("This number is divisible by 5")
    else:
        print("This is not divisible by 5")

userInput = int(input("Enter something: "))
value = executeSomething(userInput)
print("I am done")