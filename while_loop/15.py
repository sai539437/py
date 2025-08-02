str = 'hello world'

i = 0
count = 0

while i <= len(str)-1:
    if str[i] in 'aeiouAEIOU':
        count = count + 1
    i = i + 1

print('Vowel in str : ', count)