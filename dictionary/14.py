#You are asked to write a program that accepts the names and marks of students in three subjects:
#Maths, Science, and English. The program should then calculate and display the total marks and percentage for each student.
#Requirements:
#Store the data in a single dictionary (stu) where each student's name is the key.'
# The value should be another dictionary containing the student's marks for Maths, Science, and English, as well as the total marks and percentage.
#Ensure that the percentage is rounded to two decimal places.

students=int(input("enter the number of students:"))
stu={}
for i in range(students):
    name=input("Enter the name of each students from your class:")

    maths=int(input("enter the marks for maths of each students : "))
    science=int(input("enter the science marks of each students : "))
    english=int(input("enter the english marks of each students : "))

    lst = [maths,science,english]
    stu[name] = lst

for keys,values in stu.items(): # read data from dictionay and add marks in lst and print total_marks and %
    