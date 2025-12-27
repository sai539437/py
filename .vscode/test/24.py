#make a rock ,paper , scissors game with computer use for loop 
#rock beats scissors ,scissors beats paper ,paper beats rock
#make a score board system to keep track of wins losses and draws

import random

print('***welcome to the game of rock ,paper and scissors***')

choice=['rock','paper','scissors']
print('your choice:\n 0:rock \n1:paper \n2:scissors \n3:paper')

for i in range(6):
    computer_choice=random.randint(0,2)
    user_choice=int(input('enter your choice:'))
    if (user_choice==0 and computer_choice==2)or (user_choice==1 and computer_choice==0)or (user_choice==2 and computer_choice==1):
        print('you win!')
    elif user_choice==computer_choice:
        print('draw!')
    else:
        print('computer wins!')
        #scoreboard system 
        