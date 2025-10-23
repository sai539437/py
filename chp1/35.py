#user input list #no of elements #ascending descending order short 
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number of elements "))
    numbers.append(num)
a_d=sorted(numbers)
print(a_d,numbers)

