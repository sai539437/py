#create a tuple saying hello and remove e from it 
char=('H','E','L','L','O')
for i in char:
    if i=='E':
        continue
    print(i,end='')
    