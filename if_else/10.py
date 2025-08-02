#print odd and even number 
x=int(input("enter starting number"))
y=int(input("enter ending number"))
for i in range (x,y):
    if i%2==0:
        print('Even : ',i)
    else:
        print('Odd : ',i)