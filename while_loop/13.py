#ship cost calculator 

print("enter your destination")
print("Press 1 : Domestic")
print("Press 2 : Internationa")

ch=int(input("enter your choice : "))
weight=float(input("enter weight of the package in Kg only : "))

if ch==1:
    # code for domestic package cost !
    if weight>=0 and weight<=1:
        print('Cost of transportation : $5 ')
    if weight>=1 and weight<=5:
        print('cost of transportantion:$10')
    if weight<5:
        print('cost transportation is :$15')

elif ch==2:
    # code for international package cost !
    delivery=input("press 1:standard delivery\n press2: express delivery")

    if weight>=0 and weight<=1:
        print("cost of standard delivery:$15")
        print("cost of express delivery:$25")
    elif weight>=1 and weight<=5:
        print("cost of standard delivery:$30")
        print("cost of express delivery:$45")
    elif weight>5:
        print("cost of express delivery:$55")

else:
    print("invalid response")

    
