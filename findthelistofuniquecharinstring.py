#findthelistofuniquecharinstring
''' 
Write a program to count the unique charecters in a String
'''

print("Type String to calculate number of unique charecters in it:") #Printing statement
string = input().lower() #Getting Value from user and converting all of them to lower case
listofstring = [] # empty list to store data
for charecter in string: #for loop to check charecter by charecter
    if charecter not in listofstring: #if condition to check it is previously added to list or not
        listofstring.append(charecter) #adding to list if it is not present already
print("Total number of unique charecters in a given list is: ",len(listofstring)) #Printing the output
