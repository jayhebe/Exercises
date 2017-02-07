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
# regex_dedicated = re.compile(r"Bat(wo)*man")
# bo4 = regex_dedicated.findall("The Adventures of Batwowowoman, Batwowoman, Batwoman")
#  
# if bo4 != None:
#     print(bo4)
# else:
#     print("Cannot match the result.")

# regex_range = re.compile("(Ha){3,5}")
# match_result = regex_range.search("Really? HaHaHaHaHa.")
# print(match_result.group())

# str = "Hello world!!"
# match_result = re.findall("^Hello", str)
# print(match_result)

# orig_str = "This is my email address: jayhebe1983@sina.com, and you can also contact me with jayhebe1983@gmail.com."
# match_result = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", orig_str)
# 
# if len(match_result) != 0:
#     for item in match_result:
#         print(item + " is a valid email address.")
# else:
#     print(orig_str + " is not a valid email address.")

# key = r"<html><body><h1>hello world<h1></body></html>"
# p1 = r"(?<=<h1>).+?(?=<h1>)"
# pattern1 = re.compile(p1)
# matcher1 = re.search(pattern1,key)
# print(matcher1.group(0))

# key = r"<h1>hello world<h1>"
# p1 = r"<h1>.+<h1>"
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))

# key = r"jayhebe1983@sina.com.cn"
# p1 = r"@[^\.]+\."
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))

# exercise 7.17.20
# num = "1,234"
# match_result = re.search(r"\d{1,3}(,\d{3})*", num)
# print(match_result.group())

# exercise 7.17.21
# name = "Satoshi Nakamoto"
# name_pattern = r"[A-Z][A-Za-z]*\sNakamoto"
# match_result = re.search(name_pattern, name)
# print(match_result.group())

# exercise 7.17.22
# sentence = "BOB EATS CATS."
# sentence_pattern = r"(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\."
# match_result = re.search(sentence_pattern, sentence, re.IGNORECASE)
# print(match_result.group())
