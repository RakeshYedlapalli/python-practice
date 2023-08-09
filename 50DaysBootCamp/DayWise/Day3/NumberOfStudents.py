studentsList = {"Macheal":"Yes","Robert":"Yes","Sundar":"No","Gil":"Yes","Jafer":"No"}

numberOfStudents = 0;
for students in studentsList:
    if(studentsList[students] == "Yes"):
        numberOfStudents = numberOfStudents + 1
        
print("number of students in school are ->", numberOfStudents
)