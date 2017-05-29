import math, sys

def formula(num):    
    return round(math.sqrt((2 * 50 * num) / 30))

result = []
for num in list(sys.argv[1].split(",")):
    result.append(str(formula(int(num))))
    
print(",".join(result))