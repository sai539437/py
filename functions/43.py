#write a program to find the sum of even and odd number separtely in the range 100 to 500 using for loop
s=int(input("enter the number"))
sum=0
for i in range(100,501):
    if i%2==0:
        sum=sum+i
print(sum)