# remove duplicate values from list

lst = [1,1,1,2,3,4,5,5,5]
lst1=[]

for num in lst:
    if num not in lst1:
        lst1.append(num)

print(lst1)