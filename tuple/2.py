'''
Create List of Tuples with Numbers and Their Cubes
Generate tuples containing numbers and their cube values.
Output = ((1,1),(2,8),(3,27)...n)
'''
n = int(input('Enter the number : '))
tup_cube=()
tup_cu = ()
for i in range(1,n+1):
    cube = i**3
    tup_cube = tup_cube + (i, cube,)

print('Cube : ', tup_cube)