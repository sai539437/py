#ask the user the lenght of the list ,enter lenght of list,input values for lst,print lst,ask postion to edit,ask value:,
#print list with edited value

length = int(input("Enter the length of the list: "))
lst=[]
for i in range(length):
    value=int(input('Enter value to enter : '))
    lst.append(value)
print('List Created : ',lst)
pos = int(input('Enter position to edit : '))
p_value = int(input('Enter value to be added : '))

lst[pos-1]=p_value
print('Updated List : ',lst)