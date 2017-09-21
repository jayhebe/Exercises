def div_by_seven(num):
    for i in range(0, num):
        if i % 7 == 0:
            yield i
             
for result in div_by_seven(100):
    print(result)