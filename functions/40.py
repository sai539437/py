str=input("enter a string : ")
number=0
alphabets=0
for i in str:
    if i.isalpha():
        alphabets += 1
    if i.isdigit():
        number +=1

print(number,alphabets)