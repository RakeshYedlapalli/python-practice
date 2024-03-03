students = {"Rakesh":"Yes","Rajesh":"Yes","Y":"No","X":"No","Z":"Yes"}


def findNumberOfStudentsPresentInSchool(dict):
    count = 0
    for studentName in dict:
        if(dict[studentName] == "Yes"):
            count+=1
    
    return count


numberOfStudents = findNumberOfStudentsPresentInSchool(students)
print(numberOfStudents)


#extra challenge

