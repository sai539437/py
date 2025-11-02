#create a list input values from user and sort and print it 
lst=[]
x=int(input("enter the number of elements you want to choose"))
for i in range(x):
    y=int(input("enter the element"))
    lst.append(y)
    lst.sort()
print(lst)