import os, shutil

def copy_to_dest(src_path, file_type, dest_path):
    for folder_name, sub_folders, file_names in os.walk(src_path):
        for file_name in file_names:
            if file_name.endswith(file_type):
                shutil.copy(os.path.join(folder_name, file_name), dest_path)
                
copy_to_dest(r"D:\Scripts\Python\Exercises\Automate_Exercises", ".py", r"C:\123")