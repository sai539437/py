'''
make a grade system - Grade A (number greater than 90) , Grade B (number between 80 - 89), Grade C (num between 70 - 79)
Grade D (num between 60 - 69), Grade E (Better luck next time)
'''
marks=int(input("enter your marks : "))
if marks<100 and marks >90:
    print("grade A")
elif marks<89 and marks>80:
    print("grade B")
if marks<70 and marks>79:
    print("grade c")
elif marks<69 and marks>60:
    print("grade d")
elif marks<60:
    print("grade E")
    print("better luck next time")
else:
    print("invalid")

