#: Pick a Random Element from a List, also share there position a = [1, 2, 3, 4, 5, 6]
import random 
a=[1,2,3,4,5,6]
lenght=len(a)
pos=random.randrange(0,lenght)
print(pos)
print("position of the element is",pos)
