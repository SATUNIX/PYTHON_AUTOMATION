#author anthony grace 473185590
#date 3/11/2022
#splitting an input into new lines 

#variable setting 
inputstring = input("Enter the string of words\nSeperated by a fullstop:")
#variable setting into a list
a = inputstring.split(".")
#print all in the list seperated by new line
print(*a, sep = "\n")