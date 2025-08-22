# count number of alphabets in a string

str=input("enter a string : ")
a_count = 0
for i in str:
    if i.isalpha():
        a_count = a_count + 1

print('Number of alphabets in string : ', a_count)