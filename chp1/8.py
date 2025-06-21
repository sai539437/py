#traffic light stimulator:write a program that takes a color as input from the user ("red,"yellow,or green)print the action associated with that 
#colour:"red":stop yellow:prepare to red:stop if the input is no one invalid response 

t_light=input("enter your colour")

# if condition (variable operator variable/number/text) :
# elif condition :
# else :

if t_light == 'red':
    print('Stop !')
elif t_light == 'yellow':
    print('prepare to go !')
elif t_light=='green':
    print('go')
else:
    print("invalid response")