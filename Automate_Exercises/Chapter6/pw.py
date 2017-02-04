'''
author: Jay
description: py.py - An insecure password locker program
'''

import sys, pyperclip, pickle

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()
    
sys_name = sys.argv[1]

file_name = "pw_info"
with open(file_name, "rb") as pw_file:
    sys_info = pickle.load(pw_file)
    
    if sys_name in sys_info.keys():
        credential = sys_info[sys_name]
        pyperclip.copy("username: " + credential["username"] + " " + "password: " + credential["password"])
        print("The credential has been copied to clipboard.")
    else:
        print("Cannot find the credential of system " + sys_name)
        answer = input("Do you want to enter the information of system " + sys_name + "?(Y/N)")
        
        if answer.upper() == "Y":
            new_cred = {}
            username = input("Please enter the username: ")
            password = input("Please enter the password: ")
            
            new_cred["username"] = username
            new_cred["password"] = password
            
            sys_info[sys_name] = new_cred
            
            with open(file_name, "wb") as pw_file:
                pickle.dump(sys_info, pw_file)
                print("Password datebase updated.")
        elif answer.upper() == "N":
            print("Thanks for using.")
            sys.exit(1)
        else:
            print("Sorry, I cannot recognize your command.")
            sys.exit(2)