# birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}
# 
# while True:
#     name = input("Enter a name to query the birthday (blank to exit):")
#     if name == "":
#         break
#     
#     if name in birthdays:
#         print(birthdays[name] + " is the birthday of " + name)
#     else:
#         print("I do not have birthday information for " + name)
#         bday = input("What is the birthday of " + name + "?")
#         birthdays[name] = bday
#         print("birthday database updated.")

import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    if character in count.keys():
        count[character] = count[character] + 1
    else:
        count[character] = 1
        
pprint.pprint(count)