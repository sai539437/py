#a-z,65,90,A-Z,97,122,SPECIAL CHARACTER,32,64
#print(chr(65))
#print(chr(97))
import random
for i in range(2):
    value=random.randint(65,90)
    print(chr(value))
    for i in range(2):
        value=random.randint(97,122)
        print(chr(value))
        special=random.randint(32,64)
        print(chr(special))
