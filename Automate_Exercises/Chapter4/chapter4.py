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

# cat = "cat"
# spam = ["cat", "dog", "bat", "rat", "cat", "cat"]
# while cat in spam:
#     spam.remove(cat)
#     
# print(spam)

import random

message = [
           "It is certain",
           "Yes definitely",
           "Reply hazy try again",
           "Ask again later",
           "Concentrate and ask again",
           "My reply is no",
           "Outlook not so good",
           "Very doubtful"
           ]

print(message[random.randint(0, len(message) - 1)])