 #create a list with values #insert new values #uppend an element #modify/edit the existing value 
#delete an exisiting value from position #delte an position #sort the array in ascending/descending order #write a menu driven program to perform various operat


#list.insert(pos),value)
#list.position(pop)
#list.remove
#list.remove(value)
#list.sort
#list.sort(reverse)

lst=[]
len_list=int(input("enter the lenght of the list"))
for i in range((len_list)):
    value=int(input("enter your value"))
    lst.append(value)

print(lst)
while True:
    print('press 1 to insert')
    print('press 2 to position')
    print('press 3 to remove')
    print('press 4 to sort')
    ch=int(input("enter your choice"))
    if ch==1:
        print(list.insert)
    if ch==5:
        break
    else:
        print("invalid input so sad")
        
   