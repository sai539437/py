stu = {1:'sai',2:'ram',3:'sam'}
print(stu[1])

#traversing in dict
stu = {1:'sai',2:'ram',3:'sam'}
for keys in stu:
    print(stu)
for key in stu.values():
    print(key)
for key,value in stu.items():
    print(key,value)

#append / updating values in dict 
stu = {1:'sai',2:'ram',3:'sam'}
stu=[4]
print(stu)

#removing values from dict 
#using del function 
stu = {1:'sai',2:'ram',3:'sam'}
del stu[1]
print(stu)
#using pop function 
scrwe = dict(a='Sai', b='11', c='12')
scrwe.pop('a')
print(scrwe)
#membership operators in dict 

stu = {1:'sai',2:'ram',3:'sam'}
print(1 in stu)
#common dict functions 
stu = {1:'sai',2:'ram',3:'sam'}
print(len(stu))
print(stu.get(1))


#copy function 
stu = {1:'sai',2:'ram',3:'sam'}
stu1=stu
stu2=stu.copy()
print(stu1)
print(stu2)
#pop item function 
#removes last item and removes delted items 
stu = {1:'sai',2:'ram',3:'sam'}
stu.popitem()

#max function # min function 
stu = {1:'sai',2:'ram',3:'sam'} 
print(max(stu.items()))
print(min(stu.items()))

#sorted 
stu = {1:'sai',2:'ram',3:'sam'} 
print(sorted(stu))
