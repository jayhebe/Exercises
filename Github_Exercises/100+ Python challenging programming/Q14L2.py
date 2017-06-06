sentence = input()

num_upper = 0
num_lower = 0

for s in sentence:
    if s.isupper():
        num_upper += 1
    if s.islower():
        num_lower += 1
        
print("UPPER CASE " + str(num_upper))
print("LOWER CASE " + str(num_lower))