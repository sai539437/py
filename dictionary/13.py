# You are asked to write a program that accepts the names and marks of students in three subjects: 
# Maths, Science, and English. The program should then calculate and display the total marks and percentage for each student"""
# Requirements:
# Store the data in a single dictionary (stu) where each student's name is the key. 
# The value should be another dictionary containing the student's marks for Maths, Science, and English, 
# as well as the total marks and percentage.
# Ensure that the percentage is rounded to two decimal places."""

students = int(input("enter the number of students:"))  # same variable name declared multiple time
stu={}

for i in range(students):
    name=input("enter the name of each students from your class:")
    marks=int(input("enter the marks of each students:"))   # same variable name declared multiple time
    maths=int(input("enter the marks of each students in maths:"))

    if maths>90:
        print("work more hard")
    else:
        print("keep going")
    science=int(input("enter the science marks of each students:"))
    if science<95:
        print("well done")
    else:
        print("work harder")
    english=int(input("enter the english marks of each students:"))
    if english<90:
        print("bravo")
    else:
        print("needs work")
    total_marks=maths+science+english
    percentage=(total_marks/300)*100
    if marks<250:
        print("well done work more hard next time")
        if marks>100:
            print("you need to work harder")
    stu[name]={'Marks':marks,'Maths':maths,'Science':science,'English':english,}
print(stu)
