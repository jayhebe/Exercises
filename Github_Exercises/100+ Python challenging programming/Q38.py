def printtuple(mytuple):
    num = len(mytuple)
    
    print(mytuple[:(num // 2)])
    print(mytuple[(num // 2):])
    
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
printtuple(t)