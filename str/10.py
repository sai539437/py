'''
Enter a string
check if string has numbers.
if numbers found : 
    print the orignal string
    print the numbers in the string
    print the sum of the numbers
if numbers not found :
    print original string
    print message : no numbers in the string.
'''

str=input("Enter the string : ")
print(str)
sum=0
digit=[]
for i in str:
    if i.isdigit():
        i=float(i)
        digit.append(i)
        sum=sum+i
print(str)
print(digit)
print(sum)
