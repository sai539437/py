#Write a program to create a game, roll a dice. every time game rolls a dice, user need to predict the number. If numbers entered by user is same as of dice then respond - 
# umber is correct else incorrect. total of 5 chances, if user gets 3 correct prediction, user wins the games else loses the game.

import random 
x=input("welcome to game rollers")
y=int(input("enter number between 1 to 6:"))
for i in range(5):
    dice=random.randint(1,6)
    z=int(input("roll the dice and enter your prediction:"))
    if z==dice:
        print(" you guessed the number  correct")
        count=count+1
        if count==3:
            break
    else:
        print("you guessed the number incorrect")