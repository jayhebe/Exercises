def print_list(lst):
    count = 0
    result = ""
    for each_item in lst:
        if count != (len(lst) - 1):
            result += (each_item + ", ")
        else:
            result += ("and " + each_item)
        count += 1
        
    return result

spam = ["apples", "bananas", "tofu", "cats"]
print(print_list(spam))