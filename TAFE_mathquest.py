#Author = Anthony Grace
#Date = 21/11/22
#Program, display the six times table answers from to 12.
#version 1.0

#intro print and times tables options
name = str(input("Welcome to Maths Quest! What is your name? "))
#select the times table to test
n = int(input(f'{name}, which time table would you like to practice? (1-12) '))
#print the user instructions
print("Ok ", name , ": on a piece of paper, write down the ", n , " time tables from 1 to twelve. When your ready I'llshow \n you the answer so you can check your work.")
#create a while loop for the user start prompt and debug for starter input
restart = True
while restart :
    #start option for user to display the answers to the time table which was selected
    startoption = input("Are you ready to start? ('y' or 'n')")
    if startoption =="y":
        #for loop to print the  range 1-12 with the selected time table
        '''
        the for loop takes the selected number and multiplies it by i being the range 1-12 and prints it line by line
        '''
        for i in range (1, 12):
            print(n , " * " , i , " = ", n*i)
            #end the selected while loop for the  "Are you ready to start? ('y' or 'n')" function
            restart = False
    else:
        #if the user does not select 'y' to start, restart the loop and prompt the user again
        restart = True



#closing print, ends program.
close = str(input("Did you get them all correct? ('y' or 'n')"))
print("Great job ", name, " thank you for playing math quest!")

