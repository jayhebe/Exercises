import os, sys

if len(sys.argv) == 3:
    str_option = sys.argv[1]
    str_filename = sys.argv[2]
elif len(sys.argv) == 2:
    str_option = ""
    str_filename = sys.argv[1]
else:
    print("Usage: cat.py [option] filename")
    exit(1)
    
with open(os.path.abspath(str_filename)) as f:
    if str_option == "-n":
        num = 1
        for line in f.readlines():
            print(str(num).rjust(6) + "  " + line, end = "")
            num += 1
    else:
        for line in f.readlines():
            print(line, end = "")