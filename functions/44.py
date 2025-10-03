# The formula E = mc2 states that the equivalent energy (E) can be calculated as the mass (m) multiplied by the speed of light (c = about 3×108 m/s) squared.  
#Write a program that accepts the mass of an object and determines its equivalent energy.

mass = int(input('Enter the weight in kg : '))
c = 3*10**8

e = mass*c**2

print('The energy is : ',e)