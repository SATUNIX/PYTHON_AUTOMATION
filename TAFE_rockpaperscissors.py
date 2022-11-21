#Author: Anthony Grace
#Date: 3/11/22
#version: 1.0

#Rock Paper Scissors
print("lets play rock paper scissors!")
print("lets begin")

name1 = input("Player 1: What is your name?")
name2 = input("Player 2: What is your name?")

print("Hello " + name1 + " and " + name2)
print(name2 + ":Close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n")
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

if (choice1 == "r"):
    if (choice2 == "r"):
        print("The game is a draw")
    elif (choice2 == 'p'):
        print("Player 2 wins!")
    elif (choice2 == "s"):
        print("Player 1 wins!")
elif (choice1 == "p"):
    if (choice2 == "r"):
        print("Player 1 wins!")
    elif (choice2 == "p"):
        print("The game is a draw")
    elif (choice2 == "s"):
        print("Player 2 wins!")
elif (choice1 == "s"):
    if (choice2 == "r"):
        print("Player 2 wins!")
    elif (choice2 == "p"):
        print("Player 1 wins!")
    elif (choice2 == "s"):
        print("The game is a draw")
        
print("Thanks for playing Rock, Paper, Scissors")