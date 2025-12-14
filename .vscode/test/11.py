##name=James, Hazel, Blake, Eleanor, Liam, Olivia, Sonja, Barbara, Eric, and Jessica.#make a dictionary
#random roll no in squence wise , store it in dictionary ,fetch it in key and randomly print it unique number and its corresponding value 
import random 
name=["james","hazel","blake","elenaor","liam","olivia","sonha","barnara","eric","jessica"]
dictionary={}
for i in range(4):
    value=(name[i])
    key=random.randint(1000,9999)
    print(key,value)
dictionary[key]=value
print(dictionary)