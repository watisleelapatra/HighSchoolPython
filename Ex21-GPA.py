#GPA calculator
subject = int(input("How many subject do you enroll? "))
sum = 0
ca = 0
for i in range(1, subject+1) :
    print("Subject " + str(i) + " credit : ", end = '')
    credit = float(input())
    print("Subject " + str(i) + " grade : ", end = '')
    grade = input()
    if grade == 'A' :
        gr = 4
    elif grade == 'B+' :
        gr = 3.5
    elif grade == 'B' :
        gr = 3
    elif grade == 'C+' :
        gr = 2.5
    elif grade == 'C' :
        gr = 2
    elif grade == 'D+' :
        gr = 1.5
    elif grade == 'D' :
        gr = 1
    elif grade == 'F' :
        gr = 0
    gp = gr * credit
    ca = ca + credit
    sum = sum + gp
gpa = sum / ca
print("Total credit = " + str(ca) + " GPA = " + str(gpa))