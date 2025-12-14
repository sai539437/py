#School Management System (Lists & Tuples)
#A clean, minimal, menu-driven Python program to manage student records using a list of tuples.School Management System (Lists & Tuples)
#eatures
#add all the students 
    #Display all students (tabular)
    #Search student by roll number
    #Update student marks (replace the tuple)
    #Delete student record
   # Calculate totals, averages, and pass/fail status
   # Exit with a friendly message


x=input("enter the names of students in your class:")
y=int(input("enter the  admision number of each students in your class:"))
z=int(input("enter the roll number of each student of your class:"))
a=int(input("enter the marks of each student in your class:"))
students={}

while True:
    print("1.add all the students")
    print("2.display all students")
    print("3.search students by roll number")
    print("4.update student marks ")
    print("5.delete student record ")
    print("6.calculate total ,averages and pass/fail status")
    print("7 exit with a friendly message")
    choice=int(input("pls enter your choice"))
    if choice==1:
        ch = input('Enter numbe of entries of students : ')
        for i in range(ch):
            lst=[]
            x=input("enter the name of the students")
            lst.append(x)
            y=int(input("enter the roll number of each students"))
            z=int(input("enter the admission number of each students"))
            lst.append(y)
            w=int(input("enter the marks of each students"))
            lst.append(w)
            students[z]=lst

        print("students have been added successfully")
    elif  choice==2:
        print("display all students/n",students)
    elif choice==3:
        y=int(input("enter the roll number of students you want to update"))
        if y in students:
            new_marks=int(input("enter the new marks"))
            print("marks updated successfully")
        else:
            print("student record not found")
    if choice==4:
        z=int(input("enter the admission number of each students"))
        if z in students:
            del students[z]
            print("student record deleted successfully")
        else:
            print("student record not found")
    if choice==5:
        print("thank you for using our school managment system have a great day ahead")
        
            
            

        

    
