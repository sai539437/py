#linear search implementation #ask user list values #ask user to enter the value to be searched in the list # to tell if value exist or not #linear search 

lst=[10,51,2,18,4,31,13,5,23,64,29]
print(lst)

val = int(input('enter the values of list that needs to be searched : '))
count = 0
Flag = True

for i in lst:
    count=count+1
    if i == val:
        print('value : ',i,'position at : ',count)
        Flag = False
if Flag:
    print("Value not in list !")