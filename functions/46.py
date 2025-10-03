# Write a program to print the grade of 20 students when grades are allocated as given in the table below. Percentage of the marks obtained by the 20 
#students is the input to the program.
#Percentage of Marks      Grade
#Above 90%                  A
#80% to 90%                 B
#70% to 80%                 C
#60% to 70%                 D
#Below 60%                  E


s_marks=int(input("students pls enter your marks"))
if s_marks>90:
    print('you get a grade A')
elif s_marks<80 and s_marks>90:
    print('you get a grade B')
elif s_marks<70 and s_marks>80:
    print('you get a grade c')
elif s_marks>60 and s_marks<70:
    print("you get a grade d")
    print("you get a grade d")
else:
    print("work hard next time you got a grade e")
