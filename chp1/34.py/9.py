#swap the vowels a,e,i,o,u in a str


str = "hello  world"
vowels = 'aeiou'

for i in str:
    if i in vowels:
        print('@',end ='')
    else:
        print('i',end='')
      