import sys

result = []
bins = input().split(",")
for num in bins:
    if int(num, 2) % 5 == 0:
        result.append(str(num))
        
print(",".join(result))