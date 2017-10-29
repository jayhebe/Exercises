def printtuple():
    l = list()
    
    for n in range(1, 21):
        l.append(n ** 2)
        
    print(tuple(l))
    
printtuple()