# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#         
#     if text[3] != "-":
#         return False
#     
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#         
#     if text[7] != "-":
#         return False
#     
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#         
#     return True
# 
# print(isPhoneNumber("415-022-4567"))
# print(isPhoneNumber("jjj-jjj-jjjj"))
# message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
# for i in range(len(message)):
#     chunk = message[i:i + 12]
#     if isPhoneNumber(chunk):
#         print("Phone number found: " + chunk)
# print("Done")

import re

# search返回第一个匹配的结果
# phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phoneNumRegex.search("My number is 415-555-4242.")
# print("Phone number found: " + mo.group())

# 匹配可选结果，使用?，括号内的匹配字符串有无均可返回结果
# regex_single = re.compile(r"Bat(wo)?man")
# bo1 = regex_single.search("The Adventures of Batman")

# 匹配一个或多个结果，使用+
# regex_one_or_more = re.compile(r"Bat(wo)+man")
# bo2 = regex_one_or_more.search("The Adventures of Batwoman")

# 匹配零个或多个结果，使用*
# regex_zero_or_more = re.compile(r"Bat(wo)*man")
# bo3 = regex_zero_or_more.search("The Adventures of Batman")

# 匹配指定次数，可以是单个数字{3}或者范围{3,5}
# regex_dedicated = re.compile(r"Bat(wo){3}man")
# bo4 = regex_dedicated.search("The Adventures of Batwowowoman")
# 
# if bo4 != None:
#     print(bo4.group())
# else:
#     print("Cannot match the result.")

regex_range = re.compile(r"(Ha){3,5}?")
match_result = regex_range.search("Really? HaHaHaHaHa.")
print(match_result.group())