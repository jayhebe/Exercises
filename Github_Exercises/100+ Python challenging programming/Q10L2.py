sentence = input()
words = sentence.split(" ")
print(" ".join(sorted(set(words))))