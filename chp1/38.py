
#WRITE A PROGRAM TO READ A LIST OF ELEMENTS MODIFY A LIST SO IT DOES NOT CONTAIN ANY DUPLICATE EMELENT
lst = [1,1,2,3,4,4,5,6]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)

print(lst1)
