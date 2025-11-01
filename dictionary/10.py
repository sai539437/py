# wap a program to store student name marks % in dictionary and delte any student name from dictionary and display 
# dictionary details 
'''
student_marks={85:'sai',90:'ram',78:'sam',88:'manu'}
print(student_marks)
del student_marks[78]
print(student_marks)
'''

student_marks={}

# logic to enter n number of entries into dictionary
n = int(input("How many students' marks do you want to enter? "))
for i in range(n):
    student_name = input("enter your names ")
    marks = int(input("enter the marks of each students"))
    student_marks[student_name] = marks

# delete record from dictionary
x=int(input("enter the marks of the students of your class:"))
y=int(input("enter the marks of the student to be delted:"))

if y in student_marks:
    del student_marks[y]
    print(student_marks)
else:
    print("marks no available in our records")

