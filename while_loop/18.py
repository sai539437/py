#Write a program to check if a string is a palindrome or not. (A string is called palindrome if it reads same 
# backwards as forward. For example, Kanak is a palindrome.)
x='kanak'
y=x[::-1]

for i in range((len(x)-1)):
               if x[i]==y[i]:
                       print('this is a palindrome ')
               else:
                       print('this is not a palindrome')
                       
                
               
               
