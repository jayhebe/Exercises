import os

def search_file(dir_path, file_size):
    for folder_name, sub_folders, file_names in os.walk(dir_path):
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            if os.path.getsize(file_path) > file_size:
                print(file_path + " --------------------- " + str(os.path.getsize(file_path) // 1024 // 1024) + "MB")

file_size = 30 * 1024 * 1024
dir_path = r"C:\Test"
search_file(dir_path, file_size)