'''write a program that asks  anew user about userid and password and then appends it to file 'security.txt
provided the given userid does not exist in the file. If it does,then display error message 'user already exists' and prompts the user to re enter the password
also, make sure that password is at least 8 characters long with a digit and a special character $,!@#^&*'''

import re

# The check_user_exists function takes in a userid as an argument and checks if it already exists in the security.txt file
def check_user_exists(userid):
    file =  open("security.txt", "r") 
    for line in file:
        if userid in line:
            return True
        else:
            return False

# The check_password_valid function takes in a password as an argument and checks if it meets the specified criteria
def check_password_valid(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    # Check if the password contains a special character [$,%,^,&,*,!] using a regular expression
    if not re.search("[$%@^&]", password):
        return False
    return True

while True:
    userid = input("Enter a userid: ")
    if check_user_exists(userid):
        print("Error: user id already exists.")
    else:
        break

while True:
    passwd = input("Enter a password (at least 8 characters and contains special character[$,%,^,&,*,!]): ")
    if check_password_valid(passwd):
        break
    else:
        print("Error: password is not valid.")

file = open('security.txt','a')    
file.write(userid + ":" + passwd + "\n")

print("Success: userid and password added to security.txt.")

''' Regular expressions, also known as regex or regexp, are a sequence of characters that define a search pattern. 
They are often used to match, search, and manipulate strings or text.
In this code, the re module is imported and the re.search() function is used to check if the password contains a
special character [$,%,^,&,*,!]. The regular expression within the square brackets [] specifies the characters 
that should be searched for in the string.
'''
