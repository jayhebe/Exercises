# file_name = "chapter5.py"
# file_obj = open(file_name)
# print(file_obj.read())
# # print(file_obj.readlines())
# # file_obj.write("# This is the last line of the file.")
# file_obj.close()

import shelve

shelfFile = shelve.open("mydata")
cats = ["Zophie", "Pooka", "Simon"]
shelfFile["cats"] = cats
shelfFile.close()