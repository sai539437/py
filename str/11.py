str = "HEllO WORLD"
for ch in str.lower():
    if ch in 'aeiou':
        print('*', end = ' ')
    else:
        print(ch, end= ' ')
print( )