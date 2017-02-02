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

# import random
# 
# message = [
#            "It is certain",
#            "Yes definitely",
#            "Reply hazy try again",
#            "Ask again later",
#            "Concentrate and ask again",
#            "My reply is no",
#            "Outlook not so good",
#            "Very doubtful"
#            ]
# 
# print(message[random.randint(0, len(message) - 1)])

# def eggs(some_parameter):
#     some_parameter.append("hello")
#     
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

# spam = ["a", "b", "c", "d", [1, 2, 3]]
# cheese = spam[:]
# cheese[1] = 42
# print(spam)
# print(cheese)

# spam = ["a", "b", "c", "d"]
# print(spam[int("3"*2)//11])

# import copy
# 
# spam = ["a", "b", "c", "d", [1, 2, 3]]
# cheese = copy.copy(spam)
# temp = copy.deepcopy(spam)
# print(temp)
# print(cheese)