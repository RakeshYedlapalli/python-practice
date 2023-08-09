dictionary = {'rakesh':30,'rajesh':40,'mahesh':100,'suresh':39}


def findStudentAgeFromDictionary():
    studentName = input("Enter the student name as same as registered in book ")

    age = dictionary.get(studentName)
    if(age == None):
        print("We couldn't find your name in our database")
        registerStudentAge = int(input("enter your age "))
        dictionary[studentName] = registerStudentAge
        print("Hi ",studentName,", you are ", registerStudentAge," years old.")
    else:
        print("Hi ",studentName,", you are ", age," years old.")

findStudentAgeFromDictionary()