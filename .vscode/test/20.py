# ask user to enter starting limit and ending limit and generate 3 odd numbers in btw.
import random
for i in range(1):
    val1=int(input("enter the starting value"))
    val2=int(input("enter the ending value"))
    val1=random.randint(0,100)
    val2=random.randint(0,100)
    val3=random.randint(0,100)
    if val1==2:
        print("no is even")
        print(val1,val2,val3)
    else:
        if val2!=2:
            print("no is odd")
            print(val1,val2,val3)