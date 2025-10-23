scrwe = dict(a='Sai', b='11', c='12')
for key in scrwe:
    print(key)
for key in scrwe.values():
    print(key)
for key,value in scrwe.items():
    print(key,value)
del scrwe['a']
print(scrwe)

scrwe = dict(a='Sai', b='11', c='12')
scrwe.pop('a')
print(scrwe)