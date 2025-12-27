# make a rock paper scissors game with computer 
# Rock beats Scissors , Scissors beats Paper , Paper beats Rock 

import random 

sys_ch=random.randint(1,3)  # 1 : rock ,2 : scissors, 3 : paper

print(' *** Welcome to the game of rock , paper and sccissors*** ')
print(' Your chance : Enter : \n 1 : Rock \n 2 : Scissors \n 3 : Paper ')

ch = int(input("enter your choice : ")) # user choice

if (ch == 1 and sys_ch == 2) or (ch == 1 and sys_ch == 2) or (ch == 1 and sys_ch == 3):
    print(' This is a draw ! ')
    print(' User Choice : ',ch)
    print(' System Choice : ',sys_ch )
elif (ch == 2 and sys_ch == 1) or (ch == 2 and sys_ch == 2) or (ch == 2 and sys_ch == 3):
    print(' This is a draw ! ')
    print(' User Choice : ',ch)
    print(' System Choice : ',sys_ch )
elif (ch == 3 and sys_ch == 1) or (ch == 3 and sys_ch == 2) or (ch == 3 and sys_ch == 3):
    print(' This is a draw ! ')
    print(' User Choice : ',ch)
    print(' System Choice : ',sys_ch )