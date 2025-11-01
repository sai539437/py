#input mobile number and name from the user and store it in a dictionary
contacts={}
n=int(input("enter the number of contacts you want to add:"))
for i in range(n):
    name=input("enter the name:")
    mobile=int(input("enterr the mobile number:"))
    contacts[mobile]=name
print(contacts)