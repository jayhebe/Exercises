def printdict(num):
    d = dict()
    for n in num:
        d[n] = n ** 2
        
    print(d)

printdict(list(range(1, 21)))