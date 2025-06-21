'''
a websit calculates shipping cost based on toatl order value 
order under 200 rs :   shipping cost 50rs  
order between 200 and 500 shipping cost 35 rs
order over 500 rs shipping free
'''
t_cost=int(input("enter your price"))

if t_cost>200:
    print('shipping cost 50')
elif t_cost>200 and t_cost<500:
    print('shipping cost 35')
if t_cost>500:
    print('free shipping')
        