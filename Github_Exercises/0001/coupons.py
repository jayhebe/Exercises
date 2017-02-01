import string
import random

def coupons_creator(digit):
    coupon = ""
    for num in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon

def save_coupons(number):
    result = ""
    for count in range(number):
        result += (coupons_creator(12) + "\n")
    return result

with open("coupons.txt", "w") as coupon_file:
    coupon_file.write(save_coupons(200))