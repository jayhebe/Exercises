import sys

net_amount = 0

while True:
    s = input()
    if not s:
        break
    
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    
    if operation == "D":
        net_amount += amount
        
    if operation == "W":
        net_amount -= amount
        
print(net_amount)