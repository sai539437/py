# input a string from user
# write a program to count the number of characters asked from user occurs in a given string 
str='hello world'

i=0
while i<=len(str)-1:
    if str[i] in 'aeiou':
       print('*',end='')
    else:
        print(str[i],end='')
    i=1+i  