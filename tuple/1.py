'''
Write a program to read email IDs of n number of students and store them in a tuple. Create two new
tuples, one to store only the usernames from the email IDs and second to store domain names from
the email IDs. Print all three tuples at the end of the program. [Hint: You may use the function split()]
'''
emailid=()
domains=()
emails=()

n=int(input('enter the number of students:'))
for i in range(1, n+1):
    email = input('enter your email id:')
    email_id , domain = email.split('@')
    emailid=emailid+(email_id,)
    emails=emails+(email,)
    domains=domains+(domain,)
print(emails)
print(domains)
print(emailid)
