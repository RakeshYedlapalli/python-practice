def caculateTeachersSalary():
    teacherName = input("Enter teacher Name:-")
    numberOfPeriodsTaught = int(input("Number of periods taught:-"))
    defaultRatePerPeriod = 20
    monthlySalary = numberOfPeriodsTaught * defaultRatePerPeriod

    print("Teacher : ", teacherName)
    print("Period :", numberOfPeriodsTaught)
    if(numberOfPeriodsTaught > 100):
        monthlySalary +=25
    print("Gross salary :",  monthlySalary)


caculateTeachersSalary()




