import re

def my_strip(my_str, sep=" "):
    if sep == " ":
        str_pattern = r"^\s+"
        my_str = re.sub(str_pattern, "", my_str)
        str_pattern = r"\s+$"
        my_str = re.sub(str_pattern, "", my_str)
    else:
        str_pattern = sep
        my_str = re.sub(str_pattern, "", my_str)
        
    return my_str

print(my_strip("    jjjjj  bbbbb    "))