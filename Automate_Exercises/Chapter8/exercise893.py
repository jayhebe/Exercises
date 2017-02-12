import os, re

for filename in os.listdir():
#     if filename.endswith(".py"):
#         print(filename)
    if filename.endswith(".txt"):
        file_obj = open(filename)
        file_content = file_obj.read()
        pattern = r"\d{3}-\d{4}-\d{4}"
        result = re.findall(pattern, file_content)
        
        for item in result:
            print(item)