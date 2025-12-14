#write a program to read email id of n number of students and store them in tuple create two new tuples one to store username from email id 
#and second to store domain name from email id print all the three tuples at the end
n=int(input("enter the number of students:"))

# declare tuple here !!
email_id=()
username=()
domain=()

# input email here !!
for i in range(n):
    email=input("enter the email id of students:")
    user_name,domain1=email.split('@')
    username = username + (user_name,)
    domain = domain + (domain1,)
    email_id = email_id + (email,)

print(email_id,username,domain)