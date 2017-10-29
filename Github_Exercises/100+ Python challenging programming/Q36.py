def printsquare(nums):
    l = list()
    
    for n in nums:
        l.append(n ** 2)
        
    print(l[5:])
    
printsquare(list(range(1, 21)))