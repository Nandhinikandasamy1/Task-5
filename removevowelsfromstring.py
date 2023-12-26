'''
Write a python program to take string and remove all the vowels
'''
print("Type String to remove all the vowels in it.:") #Printing statement
string = input().lower() #Getting Value from user and converting all of them to lower case
vowellist = ['a', 'e','i','o','u'] #Creating list of vowels
outputstring = "" #Creating variable to store new string
for charecter in string: #Using for loop taking each charecter and assigning them to variable charecter
    if charecter not in vowellist: #Comparing the charecter with vowel list
        outputstring += charecter #If it didn't found the vowel, it will add the charecter
print("The new string without vowels: ",outputstring)#Printing the outputGuvi
        
