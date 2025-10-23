#write a menu driven a program to input name of n number of students ,total marks ,average,result ,
#store them in nested tuple , display the following menu 
#result , display , search ,merit list ,marks ,avg marks ,and then result ,pass/fail
#display name , total marks, average 
#input name , and display details of students #display all students getting above 47

n = int(input("Enter number of students: "))
stu = ()
stu1=()
for i in range(n):
    name =input("Enter the name of Student : ")
    t_marks=int(input("Enter the total marks of each students (out of 500) : "))
    avg = int(t_marks/5)
    if avg>33:
        Result = 'Pass'
    else:
        Result = 'Fail'
    stu = (name,t_marks,avg,Result,)
    stu1 = stu1+(stu,)

while True:
    print('Press 1 : Result ')
    print('Press 2 : Display Avg of Students ')
    print('Press 0 : Exit')
    ch = int(input('Enter your choice : '))
    if ch == 1:
        print('You selected 1')
    elif ch == 0:
        break
    else:
        print('invalid input !')