# def checkio(data):
#     #Your code here
#     #It's main function. Don't remove this function
#     #It's used for auto-testing and must return a result for check.  
# 
#     #replace this for solution
#     
#     for d in data:
#         if data.count(d) == 1:
#             data.pop(data.index(d))
#     
#     return data
# 
# print(checkio([1, 2, 3, 4, 5]))

import re

def checkio(data):

    #replace this for solution
    pwd_pattern = r"[a-z]+[A-Z]+[0-9]+"
    if len(data) < 10:
        return False
    else:
        if re.findall(pwd_pattern, data):
            return True
        else:
            return False
        
print(checkio("QwErTy911poqqqq"))