#write a menu driven program to input your friends name,phone number and store them in a dictionary display the name ,phone number of all friends 
#add new details of friiend modify phone number of friend 
#delete entry of friend 
#search details of friend 
#display the dictionary in sorted order

f_d={}
while True:
    print("1.add friend details")
    print("2.phone number of friend")
    print("3.delte entry of friend")
    print("4.search details of friend")
    print("5.display dictionary in sorted order")
    print("6.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter friend's name")
        phone=input("enter friend's phone number")
        f_d[name]=phone
    elif choice==2:
        name=input("enter friends name to modify phone number")
        phone=int(input("enter new phone number"))
        f_d[name]=phone
    elif choice==3:
        name=input("enter friends name to delete entry")
        phone=int(input("enter the phone number you  want to delete"))
        