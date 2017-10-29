def printdict(num):
    d = dict()
    
    for n in num:
        d[n] = n ** 2
        
    for k in d.keys():
        print(k, end = " ")
        
printdict(list(range(1, 21)))