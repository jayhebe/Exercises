keywords = ["ADJECTIVE", "NOUN", "VERB", "ADVERB"]

madlibs_temp_file = open("madlibs_temp.txt")
content = madlibs_temp_file.read()
madlibs_temp_file.close()

for keyword in keywords:
    while keyword in content:
        answer = input("Enter an " + keyword.lower() + ":")
        content = content.replace(keyword, answer)
            
madlibs_answer_file = open("madlibs_answer.txt", "w")
madlibs_answer_file.write(content)
madlibs_answer_file.close()