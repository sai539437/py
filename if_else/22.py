 ##using while loop calcualte the salary of 2 employee, ask user to enter basic salary.
# sal = basic + da(20% of basic) + hra(120% )

sal1=int(input("enter your salary"))
i=0
while i<2:
    da=i*0.2
    hra=i*1.20
    total_sal1=(sal1+da+hra)
    print(total_sal1)
    i=1+i
