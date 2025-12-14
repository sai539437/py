#make a list 5 values 2 character 3 numbers if a number is there square it and if a value is there cube it 
lst=['a',1,'b',2,'c',3]
lst1=[]
for i in lst:
    if type(i)==int:
        print(i**2 ,end=' ')
    else:
        print(i,end=' ')