def extractUserNameFromMailId ():
    emailID = input("enter email id:")
    values = emailID.split('@')
    print("values are ->", values)
    return values[0]


username = extractUserNameFromMailId()
print("Username is -> " + username)
