
#Write a program using a user defined function that displays sum of first n natural numbers, where n is passed as an argument.
def sum_of_natural_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=i
        return total

n=int(input("enter a number:"))
result=sum_of_natural_numbers(n) 
print("the sun of first",n,"natural numbers is:",result)

