s1=int(input("enter your value for side 1"))
s2=int(input("enter your value for side 2"))
s3=int(input("enter your value for side 3"))

if s1==s2 and s2==s3 and s1==s3:
    print("equilateral triangle")
elif s1 ==s2 or s1 == s3 or s2 == s3:
    print("isoceles triangle")
elif s1!=s2 and s2!=s3:
    print("scalene triangle")




