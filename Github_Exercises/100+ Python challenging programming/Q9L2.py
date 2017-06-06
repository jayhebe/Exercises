lines = []
while True:
    str = input()
    if str:
        lines.append(str.upper())
        continue
    else:
        break
    
for s in lines:
    print(s)