#Write a program that prints minimum and maximum of five numbers entered by the user


for i in range(0,5):
    value=int(input("enter the value"))
    if i==0:
        min=max=value
        if min>value:
            min=value
            if max<value:
                max=value
                print(max,min)


