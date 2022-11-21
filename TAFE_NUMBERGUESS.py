#Program: Number Guesser
#Author: Anthony Grace
#Date: 20/10/22

import random
minguess = 1
maxguess = 6

#Ask the user for their name and their guess
name = input("what is your name?")
print("Hi" , name)
print("Enter a random number between: " , minguess , "and" , maxguess)
guess = int(input("What is your guess?"))

#generate a random number and tell the user if they won or lost
secretnumber = random.randint(minguess , maxguess) 
if (guess == secretnumber):
    print("Congratulations, you got it right!")
else:
    print("you lose - the number was" , secretnumber)
    
print("thank you for playing the game")

