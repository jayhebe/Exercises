# catNames = []
# 
# while True:
#     print("Enter the name of cat " + str(len(catNames) + 1) + " or enter nothing to stop:")
#     name = input()
#     if name == "":
#         break
#     catNames = catNames + [name]
#     
# print("The cat names are: ")
# for name in catNames:
#     print(" " + name)

cat = "cat"
spam = ["cat", "dog", "bat", "rat", "cat", "cat"]
while cat in spam:
    spam.remove(cat)
    
print(spam)