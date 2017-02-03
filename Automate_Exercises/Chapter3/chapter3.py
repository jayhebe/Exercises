# def spam():
#     global eggs
#     eggs = "spam"
#     
# def bacon():
#     eggs = "bacon"
#     
# def ham():
#     print(eggs)
#     
# eggs = 42
# spam()
# print(eggs)


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    my_number = int(input("Please enter a number:"))
    
    while my_number != 1:
        my_number = collatz(my_number)
except ValueError:
    print("You must enter an integer.")