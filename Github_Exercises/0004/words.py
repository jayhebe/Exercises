# Github exercise 0002

import re

def count_words(file_name):
    count = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            word_list = re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", line)
            # word_list = re.findall("\w", line)
            count += len(word_list)
        return count
    
print(count_words("text.txt"))