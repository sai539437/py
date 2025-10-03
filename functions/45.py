#A, B, C take x days, y days and z days respectively to do the job alone. The formula to calculate the number of days if they work together is xyz/(xy + yz + xz) 
#days where x, y, and z are given as input to the program.


x=int(input("enter your number of working days"))
y=int(input("enter your working days"))
z=int(input("enter your working days"))
w=x*y*z/(x*y+y*z+x*z)
print(w)
