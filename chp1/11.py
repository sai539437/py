'''
enter user age
age = 0 to 13, m_tkt = 5          coke = 50 % discount
age 13 to 19 price 10 dollar     coke = 25 % discount 0.25
age 19 and above price 13 dollar  
'''

age = int(input("Enter your age : "))
n_ticket = int(input('Enter number of tickets : '))
n_coke = int(input('Number of coke bought : '))

coke_price = 2.5

if age>0 and age<=13 :
    total_ticket_price = n_ticket * 5
    total_coke_price = (n_coke * coke_price) * 0.05
    total_amt = total_coke_price + total_ticket_price
if age>13 and age<=19:
    total_ticket_price=n_ticket*10
    toatl_coke_price=(n_coke*coke_price)*0.25
    total_amt=total_coke_price+ total_ticket_price
if age>19:
    total_ticket_price=n_ticket*13
    toatl_coke_price=(n_coke*coke_price)*0.13
    total_amt=toatl_coke_price+toatl_coke_price


print('Total Movie Ticket Price : ', total_ticket_price)
print('Total Coke Price : ', total_coke_price)
print('Total Ammout : ', total_amt)
