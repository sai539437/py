#Input:  deleteChar("Hello World", "l")
#Output: "Heo Word"

str = input('Enter a string : ')
ch = input('Enter character to delete from string : ')

for i in str :
    if ch == i:
        continue
    else:
        print(i, end=' ')
print(' ')