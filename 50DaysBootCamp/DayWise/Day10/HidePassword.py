def hidePassword():
    password = input("Enter the password to be encrypt: ")
    print("Entered password is =>", password)

    print("Enrypted password is -> " , '*'*len(password))
    print("Length of the password is => ", len(password))

hidePassword()