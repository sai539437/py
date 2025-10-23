#wap to input names of an employes and their salary [basic salary,house rent,allowance],calucalatr toatl salary of each employee and display the salary 

employees = {}
n = int(input("Enter number of employees: "))

for i in range(n):
    str = []
    name = input("enter your name")
    basic_salary = int(input("enter your baisc salary"))
    str.append(basic_salary)
    house_rent = int(input("enter your house rent"))
    str.append(house_rent)
    allowance = int(input("enter your monthly allowance"))
    str.append(allowance)
    employees[name] = str

for keys,values in employees.items():
    sum=0
    for i in values:
        sum=sum + i
    print(keys, sum)