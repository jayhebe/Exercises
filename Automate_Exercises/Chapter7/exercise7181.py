import re

def pwd_detection(password):
    if len(password) < 8:
        return False
    
    pwd_pattern = r"[A-Z]+[a-z]+[0-9]+"
    result = re.search(pwd_pattern, password)
    if result != None:
        return True
    else:
        return False
    
password = "Start1234"

if pwd_detection(password):
    print("OK.")
else:
    print("Not OK.")