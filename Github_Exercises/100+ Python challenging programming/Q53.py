# email = input("Please input your email: ")
# 
# name = email.split("@")[0]
# 
# print(name)

import re
 
email = input("Please input your email: ")
pattern = "(\w+)@((\w+\.)+(com))"
result = re.match(pattern, email)
print(result.group(1))