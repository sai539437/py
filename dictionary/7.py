
# Write a Python program to extract a list of values from a given list of dictionaries.

#Original Dictionary:
sub=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
for i in sub:
    print(i['Science'])
for keys in sub:
    print(keys)
for keys,items in sub:
    print(keys,items)
sub_science=[d.get('science')for d in sub]
print(sub_science)