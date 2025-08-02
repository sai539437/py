def conical(radius,lenght):
    csa_conical=3.14*radius*lenght
    return csa_conical
def cylindrical(radius,height):
    csa_cylinderical=2*3.14*radius*height
    return csa_cylinderical
def total_price(area):
    unit_price=int(input("enter the unit_price of tent"))
    total_price=canvas*unit_price
    final_price=total_price+(0.18*total_price)
    print("the total_price of canvas")
    print("the total_price of tent with gst")
          

#main program
r = int(input("enter radius"))
l = int(input("enter lenght"))
h = int(input("enter height"))
canvas = conical(r,l) + cylindrical(r,h)
total_price(canvas)

