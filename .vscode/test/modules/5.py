#make a guess game #number between 1-10
import random
number_to_guess=random.randint(1,10)
user_choice=int(input("guess a number between 1 and 10"))
if user_choice==number_to_guess:
    print("bravo you have guessedd the number right")
else:
    print("better luck next time ")
    print("your number was",number_to_guess)
    