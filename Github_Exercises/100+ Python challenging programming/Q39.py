def printtuple(mytuple):
    l = list()
    
    for num in mytuple:
        if num % 2 == 0:
            l.append(num)
            
    print(tuple(l))
    
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
printtuple(t)