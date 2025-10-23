#wap a program to count the no of times a character appears in a string using dictionary 
str= input("Enter a string: ")
char_count = {}
for ch in str:
    if ch in char_count:
        if ch not in char_count:
            str.count(ch)
            char_count(str=char_count)
print(char_count) 
        
