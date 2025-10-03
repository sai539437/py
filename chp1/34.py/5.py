# count the number of value occrence in a tuple
# tup = (1,1,1,2,2,3,3,4,5,6,7,7,7,7,7)
# 1 is present 3 times in the tuple

tup = (1,1,1,2,2,3,3,4,5,6,7,7,7,7,7)
lst=[]

for i in tup:
    if i not in lst:
        print('Value : ',i, 'has ',tup.count(i),' count in the tuple')
    lst.append(i)
