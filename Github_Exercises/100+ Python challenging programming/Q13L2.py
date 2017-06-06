sentence = input()
num_letter = 0
num_digit = 0
for s in sentence:
    if s.isalpha():
        num_letter += 1
    if s.isdigit():
        num_digit += 1
        
print("LETTERS " + str(num_letter))
print("DIGITS " + str(num_digit))