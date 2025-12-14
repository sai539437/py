#name=James, Hazel, Blake, Eleanor, Liam, Olivia, Sonja, Barbara, Eric, and Jessica.#put it in lst=[] one by one use print any 4 random names from the list 

import random
lst=["james","hazel","blake","elenaor","liam","olivia","sonha","barbara","eric","jessica"]
for i in range(4):
    value = random.randint(0,len(lst)-1)
    print(lst[value])
