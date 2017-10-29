def printdict(num):
    d = dict()
    for n in num:
        d[n] = n ** 2
        
    for v in d.values():
        print(v, end = " ")

printdict(list(range(1, 21)))