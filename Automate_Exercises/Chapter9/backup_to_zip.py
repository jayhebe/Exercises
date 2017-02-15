import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + "_" + str(number) + ".zip"
        
        if not os.path.exists(zip_file_name):
            break
        number = number + 1
        
    # TO DO: Create the ZIP file.
    print("Creating %s..." % (zip_file_name))
    backup_zip = zipfile.ZipFile(zip_file_name, "w")
    
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % (foldername))
        backup_zip.write(foldername)
        
    for filename in filenames:
        new_base = os.path.basename(folder) + "_"
        if filename.startswith(new_base) and filename.endswith(".zip"):
            continue
        backup_zip.write(os.path.join(foldername, filename))
        
    backup_zip.close()
    print("Done.")
    
backup_to_zip(r"C:\example")