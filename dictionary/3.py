# Write a program to enter name of employes and their salary as input and store them in dict 

num_empl = {}
num_empl1 = int(input("Enter the number of employees: "))
for i in range(num_empl1):
    name = input("Enter employee name: ")
    salary = int(input("enter your salary"))
    num_empl[name]=salary 
print(num_empl)
