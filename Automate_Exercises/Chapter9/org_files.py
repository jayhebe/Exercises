import os

def my_walk(dir_path):
    print("The current folder is " + dir_path)
     
    for item in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, item)):
            print("SUBFOLDER OF " + dir_path + ": " + item)
            my_walk(os.path.join(dir_path, item))
        else:
            print("FILE INSIDE " + item)
             
    print("")
    
my_walk(r"C:\Study\Programming\Python\Exercises\Automate_Exercises")