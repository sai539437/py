#create a list of tuple with numbers and their cube
# [(1,1),(2,8),(3,27)]
lst=[]
for i in range(1,11):
    lst.append((i,i**3))
print(lst)