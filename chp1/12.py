"""user input regular customer or member if regualar customer 0-50 purchase 5% above 50-100 10% and 100_to above20%"""


purchase_amount=float(input("enter purchage amount : "))
discount=0

if customer =="regular":
    if purchase_amount>=0 and purchase_amount<=50:
        t_amt = purchase_amount
    elif purchase_amount>=50 and purchase_amount<=100:
              d_amount=purchase_amount*0.05
              t_amt=purchase_amount-d_amount    
    elif purchase_amount>=100:
              d_amount=purchase_amount*0.1
              t_amt=purchase_amount-d_amount

print("toatl_p_amt:",t_amt)