import string

def check_password(password):    
    if len(password) < 6 or len(password) > 12:
        return False
    
    num_lower = 0
    num_upper = 0
    num_digit = 0
    num_special = 0
    
    for letter in password:
        if letter in string.ascii_lowercase:
            num_lower += 1
            continue
        
        if letter in string.ascii_uppercase:
            num_upper += 1
            continue
        
        if letter in string.digits:
            num_digit += 1
            continue
        
        if letter in "$#@":
            num_special += 1
            continue
        
    if 0 in [num_lower, num_upper, num_digit, num_special]:
        return False
    else:
        return True
    

passwords = input().split(",")
valid_passwords = [pwd for pwd in passwords if check_password(pwd)]
print(",".join(valid_passwords))
