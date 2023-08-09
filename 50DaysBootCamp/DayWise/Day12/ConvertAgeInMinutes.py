def convertAgeToMinutes():
    age = input("enter your age:")
    ageInIntegers = int(age)
    #print("age is =>", ageInIntegers)
    return ageInIntegers * 365 * 24 * 60

result = convertAgeToMinutes()
print("age in minutes is ->", result)