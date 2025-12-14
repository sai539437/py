#5 random number add in list and range starting end has to be defined by the user 

import random

x=int(input("enter the starting range"))
y=int(input("enter the ending range"))

random_list=[] # empty list
for i in range(5):
    random_value = random.randint(x,y)
    if random_value%2 == 0: # checking if random_value holds even number.
        random_list.append(random_value)

print("your number is",random_list)