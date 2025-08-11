#ask user to enter number of students then accept their marks for each student ,and store them in a list print the entered students marks ask students to enter any specific students marks 
#print updated list

n = int(input("Enter the number of students: "))
marks=[]

for i in range(n):
    input_marks=int(input("enter marks for student"))
    marks.append(input_marks)
print("input_marks",marks)
a=int(input("enter marks to be removed"))
marks.remove(a)
print("marks",marks)

print("this is the updated list")
