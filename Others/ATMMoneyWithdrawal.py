import time

print("Please insert your ATM Card..")

pinNumber = 2023
maxAmount = 100

atmCard = input()

print("Please wait.....")
time.sleep(3)

print("Enter your ATM Pin number")

userPinNumber = int(input())

print("Validation the pin number.....")
time.sleep(3)
if (userPinNumber == pinNumber):

    print("Pin number is correct so processing it....")
    print("enter the amount to be withdrawl")

    requestedAmount = int(input())
    if (requestedAmount < maxAmount):
        print("Collect the amount")
    elif (True):
        print("I am in elif")
    else:
        print("Insufficient funds")

else:
    print("Entered pin is incorrect")
