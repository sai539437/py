'''
customer : regular / premium
regular : order value - 50 and above : 20%
pre - order value : 50 and above : 30%
'''
print('Welcome to CMS Store')
print('Press 1 : Regular Customer ')
print('Press 2 : premium customer')
ch=int(input("enter your choice 1 or 2 : "))
if ch==1:
    x=int(input("enter your order value : "))
    if x>50:
        print("you get a discount of 20%")
    else:
        print("you get no discount")
elif ch==2:
    x=int(input("enter your order value :"))
    if x>50:
        print("you get a discount of 30%")
    else:
        print("you  get no discount")
