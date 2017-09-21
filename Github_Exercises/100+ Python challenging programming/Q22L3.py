import re, pprint

sentence = input("Please enter a sentence: ")
result = {}

word_pattern = "\S+"
words = re.findall(word_pattern, sentence)

for word in words:
    if word in result:
        result[word] += 1
    
    result.setdefault(word, 1)
    
pprint.pprint(result)