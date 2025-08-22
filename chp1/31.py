str='hello world123'
count=0
d_count=0
for i in str:
    if i.isalpha():
        count=count+1
    if i.isdigit():
        d_count=d_count+1       

print(count)
print(d_count)
