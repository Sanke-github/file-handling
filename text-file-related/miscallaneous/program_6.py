import re

def check_user_exists(userid):
    file =  open("security.txt", "r") 
    for line in file:
        if userid in line:
            return True
        else:
            return False

def check_password_valid(password):
    if len(password) < 8:
        return False
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
