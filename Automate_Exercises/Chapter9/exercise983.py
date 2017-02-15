import os, shutil

def make_seq_num(file_prefix, file_path):
    num = 0
    
    for file_name in os.listdir(file_path):
        num = num + 1
        if file_name.startswith(file_prefix):
            file_suffix = file_name[file_name.index("."):]
            new_file_prefix = file_prefix + str(num)
            if file_name.startswith(new_file_prefix):
                continue
            else:
                old_file_name = os.path.join(file_path, file_name)
                new_file_name = os.path.join(file_path, (new_file_prefix + file_suffix))
#                 print("Renaming '%s' to '%s'..." % (old_file_name, new_file_name))
                shutil.move(old_file_name, new_file_name)
                
make_seq_num("spam00", r"C:\Study\Programming\Python\Exercises\Automate_Exercises\Chapter9\Test")