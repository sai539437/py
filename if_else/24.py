# factorial

x=int(input("enter a number"))

i = 1
fact = 1
while i<=x:
    fact = fact * i
    i = i + 1

print('Factorial : ',fact)