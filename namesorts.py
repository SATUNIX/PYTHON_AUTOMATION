#author = anthony
# date = 3 /11

#use input
mylist = input(str("Enter your words here seperates by a space:"))
#seperate words by the spaces 
mylistsep = mylist.split (" ")
# sort the list of words by alphabetical order 
sorted_list = sorted(mylistsep)
#loop to print the list seperated by a new line without the new line tag
for word in sorted_list:
    print(word)