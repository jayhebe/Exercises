import sys, pyperclip, shelve

file_name = "my_clipboard"

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage mcb.py [save|list|<keyword>]")
    exit(1)
    
elif len(sys.argv) == 2:
    if sys.argv[1] == "list":
        # TO DO: list all keyword
        cb_file = shelve.open(file_name)
        for keyword in list(cb_file.keys()):
            print(keyword)
            
        cb_file.close()
    else:
        keyword = sys.argv[1]
        # TO DO: copy the content of keyword to clipboard
        cb_file = shelve.open(file_name)
        
        try:
            pyperclip.copy(cb_file[keyword])
            print("Clipboard content copied.")
        except KeyError:
            print("Cannot find keyword '" + keyword + "'")
            exit(2)
        
        cb_file.close()
        
elif len(sys.argv) == 3:
    if sys.argv[1] != "save":
        print("Cannot recognize your command.")
        print("Usage mcb.py [save|list|<keyword>]")
        exit(3)
    else:
        # TO DO: save the content of keyword to file
        cb_file = shelve.open(file_name)
        cb_file[sys.argv[2]] = pyperclip.paste()
        print("Clipboard content of keyword  '" + sys.argv[2] + "' saved.")
        cb_file.close()