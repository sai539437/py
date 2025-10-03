# palindrome

str = input('Enter a string for palindrome : ')
if str == str[::-1]:
    print(str,': this is palindrome')
else:
    print(str,': Not a palindrome !')