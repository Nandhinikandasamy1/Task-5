''' Write a python program to check palindrome of the string. Print true if it is palidrome, false if it is not'''

print("Type String to calculate number of unique charecters in it:") #Printing statement
string = input().lower() #Getting Value from user and converting all of them to lower case
reversedstring = "" #empty variable to store reverse string
for i in string: #loop to add the charecters in reverse order
    reversedstring = i + reversedstring
 
if (string == reversedstring):#Condition to check both strings
    print("True")
else:
    print("False")
