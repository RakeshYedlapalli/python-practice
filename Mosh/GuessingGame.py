value = 9
attempts = 0

while attempts < 3:
    guessValue = input("Enter the guess value ")

    if(guessValue == "9"):
        print("You win")
        exit()
    
    attempts += 1
else:
    print("You exceeded the attempts which is 3")