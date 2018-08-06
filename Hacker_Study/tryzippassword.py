import zipfile, sys


def read_password(password_file):
    with open(password_file, "rb") as pf:
        password_list = pf.readlines()
        
    return password_list


def test_zip_password(zip_file, password_list):
    for password in password_list:
        try:
            zipfile.ZipFile(zip_file).extractall(pwd=password[:-1])
        except:
            continue
        
        return password[:-1].decode()


if __name__ == "__main__":
    zip_file_path, password_file_path = sys.argv[1:]
    passwords = read_password(password_file_path)
    password = test_zip_password(zip_file_path, passwords)
    
    if password is not None:
        print("The password of file %s is %s" % (zip_file_path, password))
    else:
        print("Cannot find password of file %s" % zip_file_path)
