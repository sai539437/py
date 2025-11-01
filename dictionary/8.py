#Original Dictionary : {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
#Update the list values of the said dictionary : {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

sub ={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
sub1={}

for keys,values in sub.items():
    marks=[]
    for i in values:
        marks.append(i+1)
        sub1[keys]=marks

print(sub1)
