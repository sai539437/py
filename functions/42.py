s=int(input("enter your sales amount"))
if s>3000:
    print('25% of salesmat')
elif s<25000 and s>30000:
    print('20% of salesmat')
elif s>15000 and s<249999:
    print('15% of salesmat')
elif s>5000 and s<14999:
    print('10% of salesmat')
else:
    print('no commission')