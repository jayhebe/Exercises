def print_square(num):
    result = {}
    
    for i in range(1, num + 1):
        result[i] = i * i
        
    return result

print(print_square(8))