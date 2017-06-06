numbers = input().split(",")

# result = []
# for num in numbers:
#     if int(num) % 2 == 1:
#         result.append(num)

result = [num for num in numbers if int(num) % 2 == 1]    
print(",".join(result))