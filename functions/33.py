#leap year 
yr = int(input("enter the year"))
if (yr % 4 == 0) and ((yr % 100 != 0) or (yr % 400 == 0)):
    print('this is leap yr')
else:
    print('not a leap yr !')