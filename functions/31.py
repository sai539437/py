'''
Write a program to generate the sequence: –5, 10,–15, 20, –25….. upto n, where n is an integer input
by the user.
'''

value = int(input('Enter the value of n : '))

for i in range(1, value+1):
    if i%2 == 0:
        print(i*5)
    else:
        print(i*-5)