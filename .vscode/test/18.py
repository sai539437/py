#    🎯 Number Quest Funcation -
 #   A list stores possible numbers.
#lst = [ 11,22,33,44,55,66,77 ]
   # The computer randomly selects one number.
   # The student guesses the number.
  #  Score is stored in a dictionary.   

lst=[11,22,33,44,55,66,77]
import random
x=int(input("enter a number from the list[11,22,33,44,55,66,77]:"))
y=random.randint(11,77)
z=int(input("enter your choice"))
if x==lst[z]:

    print("you guessed the number correctly")
else:
    print("you guessed the number wrong")
    